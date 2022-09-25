import os
from pathlib import Path
import random
import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
from tqdm import tqdm
import torch
from torch.utils.data import DataLoader, Dataset
import torch.nn as nn
import torch.nn.functional as F
from hydrodataset.camels import Camels
import HydroErr as he

DEVICE = torch.device(
    "cuda:0" if torch.cuda.is_available() else "cpu"
)  # check if GPU is available


class CamelsDataset(Dataset):
    """Base data set class to load and preprocess data (batch-first) using PyTroch's Dataset"""

    def __init__(
        self,
        basins: list,
        dates: list,
        data_attr: pd.DataFrame,
        data_forcing: xr.Dataset,
        data_flow: xr.Dataset,
        loader_type: str = "train",
        seq_length: int = 100,
        means: pd.DataFrame = None,
        stds: pd.DataFrame = None,
    ):
        """
        Initialize Dataset containing the data of multiple basins.

        Parameters
        ----------
        basins : list
            _description_
        dates : list
            _description_
        data_attr : pd.DataFrame
            _description_
        data_forcing : xr.Dataset
            _description_
        data_flow : xr.Dataset
            _description_
        loader_type : str, optional
            _description_, by default "train"
        seq_length : int, optional
            _description_, by default 100
        means : pd.DataFrame, optional
            _description_, by default None
        stds : pd.DataFrame, optional
            _description_, by default None

        Raises
        ------
        ValueError
            _description_
        """
        super(CamelsDataset, self).__init__()
        if loader_type not in ["train", "valid", "test"]:
            raise ValueError(
                " 'loader_type' must be one of 'train', 'valid' or 'test' "
            )
        else:
            self.loader_type = loader_type
        self.basins = basins
        self.dates = dates

        self.seq_length = seq_length

        self.means = means
        self.stds = stds

        self.data_attr = data_attr
        self.data_forcing = data_forcing
        self.data_flow = data_flow

        # load and preprocess data
        self._load_data()

    def __len__(self):
        return self.num_samples

    def __getitem__(self, item: int):
        basin, time = self.lookup_table[item]
        seq_length = self.seq_length
        x = (
            self.x.sel(
                basin=basin,
                time=slice(time, time + np.timedelta64(seq_length - 1, "D")),
            )
            .to_array()
            .to_numpy()
        ).T
        c = self.c.loc[basin].values
        c = np.tile(c, (seq_length, 1))
        xc = np.concatenate((x, c), axis=1)
        y = (
            self.y.sel(
                basin=basin,
                time=time + np.timedelta64(seq_length - 1, "D"),
            )
            .to_array()
            .to_numpy()
        )
        return torch.from_numpy(xc).float(), torch.from_numpy(y).float()

    def _load_data(self):
        """load data from nc and feather files"""
        if self.loader_type == "train":
            train_mode = True
            df_mean_forcings = self.data_forcing.mean().to_pandas()
            df_std_forcings = self.data_forcing.std().to_pandas()
            df_mean_streamflow = self.data_flow.mean().to_pandas()
            df_std_streamflow = self.data_flow.std().to_pandas()
            df_mean_attr = self.data_attr.mean()
            df_std_attr = self.data_attr.std()
            self.means = pd.concat([df_mean_forcings, df_mean_attr, df_mean_streamflow])
            self.stds = pd.concat([df_std_forcings, df_std_attr, df_std_streamflow])
        else:
            train_mode = False

        # nomalization
        self.x = self._local_normalization(
            self.data_forcing, list(self.data_forcing.keys())
        )
        self.c = self._local_normalization(
            self.data_attr, self.data_attr.columns.values.tolist()
        )
        if train_mode:
            self.y = self._local_normalization(
                self.data_flow, list(self.data_flow.keys())
            )
        else:
            self.y = self.data_flow
        self.train_mode = train_mode
        self._create_lookup_table()

    def _local_normalization(self, feature, variable) -> np.ndarray:
        """Normalize features with local mean/std."""
        feature = (feature - self.means[variable]) / self.stds[variable]
        return feature

    def _create_lookup_table(self):
        """create a index table for __getitem__ functions"""
        lookup = []
        # list to collect basins ids of basins without a single training sample
        seq_length = self.seq_length
        dates = self.data_flow["time"].to_numpy()
        time_length = len(dates)
        for basin in tqdm(self.basins):
            for j in range(time_length - seq_length + 1):
                lookup.append((basin, dates[j]))
        self.lookup_table = {i: elem for i, elem in enumerate(lookup)}
        self.num_samples = len(self.lookup_table)

    def get_means(self):
        return self.means

    def get_stds(self):
        return self.stds

    def local_denormalization(self, feature, variable="streamflow"):
        """revert the normalization for streaflow"""
        feature = feature * self.stds[variable] + self.means[variable]
        return feature


class LSTM_CAMELS(nn.Module):
    """Implementation of a two-layer LSTM network"""

    def __init__(self, input_size, hidden_size: int, dropout_rate: float = 0.0):
        """Construct LSTM-CAMELS

        Parameters
        ----------
        input_size : _type_
            _description_
        hidden_size : int
            _description_
        dropout_rate : float, optional
            _description_, by default 0.0
        """
        super(LSTM_CAMELS, self).__init__()

        # create required layer
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=2,
            bias=True,
            batch_first=True,
        )
        self.dropout = nn.Dropout(p=dropout_rate)
        self.fc = nn.Linear(in_features=hidden_size, out_features=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through the Network"""
        output, (h_n, c_n) = self.lstm(x)

        # perform prediction only at the end of the input sequence
        pred = self.fc(self.dropout(h_n[-1, :, :]))
        return pred


def train_epoch(model, optimizer, loader, loss_func, epoch):
    """Train model for a single epoch"""
    # set model to train mode (important for dropout)
    model.train()
    pbar = tqdm(loader)
    pbar.set_description(f"Epoch {epoch}")
    # request mini-batch of data from the loader
    for xs, ys in pbar:
        # delete previously stored gradients from the model
        optimizer.zero_grad()
        # push data to GPU (if available)
        xs, ys = xs.to(DEVICE), ys.to(DEVICE)
        # get model predictions
        y_hat = model(xs)
        # calculate loss
        loss = loss_func(y_hat, ys)
        # calculate gradients
        loss.backward()
        # update the weights
        optimizer.step()
        # write current loss in the progress bar
        pbar.set_postfix_str(f"Loss: {loss.item():.4f}")


def eval_model(model, loader):
    """Evaluate the model"""
    # set model to eval mode (important for dropout)
    model.eval()
    obs = []
    preds = []
    # in inference mode, we don't need to store intermediate steps for
    # backprob
    with torch.no_grad():
        # request mini-batch of data from the loader
        for xs, ys in loader:
            # push data to GPU (if available)
            xs = xs.to(DEVICE)
            # get model predictions
            y_hat = model(xs)
            obs.append(ys)
            preds.append(y_hat)

    return torch.cat(obs), torch.cat(preds)


def load_streamflow(ds_flow, ds_attr, basins, time_range):
    """load streamflow data in the time_range and transform its unit from ft3/s to mm/day

    Parameters
    ----------
    ds_flow : _type_
        _description_
    ds_attr : _type_
        _description_
    time_range : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    chosen_streamflow = ds_flow.sel(
        basin=basins, time=slice(time_range[0], time_range[1])
    )
    area = ds_attr["area_gages2"].values
    flow = (
        0.0283168
        * chosen_streamflow
        * 1000
        * 86400
        / (area.reshape(len(area), 1) * 10**6)
    )
    return flow


def set_random_seed(seed):
    """
    Set a random seed to guarantee the reproducibility

    Parameters
    ----------
    seed
        a number
    Returns
    -------
    None
    """
    print("Random seed:", seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


set_random_seed(1234)
camels_us_path = os.path.join("camels", "camels_us")
us_region = "US"
camels_us = Camels(camels_us_path, region=us_region)
data_dir = camels_us.data_source_dir
streamflow_ds = xr.open_dataset(data_dir.joinpath("camels_streamflow.nc"))
forcing_ds = xr.open_dataset(data_dir.joinpath("camels_daymet_forcing.nc"))
attrs = pd.read_feather(data_dir.joinpath("camels_attributes_v2.0.feather"))

basins_num = 2

chosen_basins = camels_us.camels_sites["gauge_id"][:basins_num].values
train_times = ["1990-09-01", "2000-08-31"]
valid_times = ["2000-09-01", "2005-08-31"]
chosen_forcing_vars = ["dayl", "prcp", "srad", "tmax", "tmin", "vp"]
chosen_attrs_vars = [
    "p_mean",
    "p_seasonality",
    "frac_snow",
    "aridity",
    "geol_porostiy",
    "geol_permeability",
    "soil_depth_statsgo",
    "soil_porosity",
    "soil_conductivity",
    "elev_mean",
    "slope_mean",
    "area_gages2",
    "frac_forest",
    "lai_max",
]

chosen_attrs = attrs[attrs["gauge_id"].isin(chosen_basins)][
    ["gauge_id"] + chosen_attrs_vars
]
chosen_attrs = chosen_attrs.set_index("gauge_id")
train_forcings = forcing_ds[chosen_forcing_vars].sel(
    basin=chosen_basins, time=slice(train_times[0], train_times[1])
)
valid_forcings = forcing_ds[chosen_forcing_vars].sel(
    basin=chosen_basins, time=slice(valid_times[0], valid_times[1])
)
train_flow = load_streamflow(streamflow_ds, chosen_attrs, chosen_basins, train_times)
valid_flow = load_streamflow(streamflow_ds, chosen_attrs, chosen_basins, valid_times)

# settings
input_size = len(chosen_attrs_vars) + len(chosen_forcing_vars)
hidden_size = 10  # Number of LSTM cells
dropout_rate = 0.0  # Dropout rate of the final fully connected Layer [0.0, 1.0]
learning_rate = 1e-3  # Learning rate used to update the weights
sequence_length = 100  # Length of the meteorological record provided to the network
batch_size = 32

# Training data
ds_train = CamelsDataset(
    basins=chosen_basins,
    dates=train_times,
    data_attr=chosen_attrs,
    data_forcing=train_forcings,
    data_flow=train_flow,
    loader_type="train",
    seq_length=sequence_length,
    means=None,
    stds=None,
)
tr_loader = DataLoader(ds_train, batch_size=batch_size, shuffle=True)
# Validation data
means = ds_train.get_means()
stds = ds_train.get_stds()
ds_val = CamelsDataset(
    basins=chosen_basins,
    dates=valid_times,
    data_attr=chosen_attrs,
    data_forcing=valid_forcings,
    data_flow=valid_flow,
    loader_type="valid",
    seq_length=sequence_length,
    means=means,
    stds=stds,
)
valid_batch_size = 1000
val_loader = DataLoader(ds_val, batch_size=valid_batch_size, shuffle=False)

# Here we create our model, feel free
model = LSTM_CAMELS(
    input_size=input_size, hidden_size=hidden_size, dropout_rate=dropout_rate
).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
loss_func = nn.MSELoss()

n_epochs = 2  # Number of training epochs

for i in range(n_epochs):
    train_epoch(model, optimizer, tr_loader, loss_func, i + 1)
    obs, preds = eval_model(model, val_loader)
    preds = ds_val.local_denormalization(preds.cpu().numpy(), variable="streamflow")
    obs = obs.numpy().reshape(basins_num, -1)
    preds = preds.reshape(basins_num, -1)
    nse = np.array([he.nse(preds[i], obs[i]) for i in range(obs.shape[0])])
    tqdm.write(f"Validation NSE mean: {nse.mean():.2f}")


# Evaluate on test set
test_times = ["2005-09-01", "2010-08-31"]
test_forcings = forcing_ds[chosen_forcing_vars].sel(
    basin=chosen_basins, time=slice(test_times[0], test_times[1])
)
test_flow = load_streamflow(streamflow_ds, chosen_attrs, chosen_basins, test_times)
ds_test = CamelsDataset(
    basins=chosen_basins,
    dates=test_times,
    data_attr=chosen_attrs,
    data_forcing=test_forcings,
    data_flow=test_flow,
    loader_type="test",
    seq_length=sequence_length,
    means=means,
    stds=stds,
)
test_batch_size = 1000
test_loader = DataLoader(ds_test, batch_size=test_batch_size, shuffle=False)
obs, preds = eval_model(model, test_loader)
preds = ds_test.local_denormalization(preds.cpu().numpy(), variable="streamflow")
obs = obs.numpy().reshape(basins_num, -1)
preds = preds.reshape(basins_num, -1)
nse = np.array([he.nse(preds[i], obs[i]) for i in range(obs.shape[0])])

# Plot results
start_date = pd.to_datetime(ds_test.dates[0], format="%Y-%m-%d") + pd.DateOffset(
    days=sequence_length - 1
)
end_date = pd.to_datetime(ds_test.dates[1], format="%Y-%m-%d")
date_range = pd.date_range(start_date, end_date)
for i in range(basins_num):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(date_range, obs[i], label="observation")
    ax.plot(date_range, preds[i], label="prediction")
    ax.legend()
    ax.set_title(f"Basin {chosen_basins[i]} - Test set NSE: {nse[i]:.3f}")
    ax.xaxis.set_tick_params(rotation=45)
    ax.set_xlabel("Date")
    _ = ax.set_ylabel("Streamflow (mm/d)")
    save_dir = Path(os.path.abspath(__file__)).parent
    plt.savefig(
        save_dir.joinpath(chosen_basins[i] + "_streamflow_timeseries.png"),
        dpi=600,
        bbox_inches="tight",
    )

# 初探Pytorch

## 什么是Pytorch？

Pytorch是torch的python版本，是由Facebook开源的神经网络框架，专门针对 GPU 加速的深度神经网络（DNN）编程。Torch 是一个经典的对多维矩阵数据进行操作的张量（tensor ）库，在机器学习和其他数学密集型应用有广泛应用。与Tensorflow的静态计算图不同，pytorch的计算图是动态的，可以根据计算需要实时改变计算图。但由于Torch语言采用 Lua，导致在国内一直很小众，并逐渐被支持 Python 的 Tensorflow 抢走用户。作为经典机器学习库Torch 的端口，PyTorch 为 Python 语言使用者提供了舒适的写代码选择。

## 为什么选择Pytorch？

- 简洁
PyTorch的设计追求最少的封装，尽量避免重复造轮子。不像 TensorFlow 中充斥着session、graph、operation、name_scope、variable、tensor、layer等全新的概念，PyTorch 的设计遵循tensor→variable(autograd)→nn.Module 三个由低到高的抽象层次，分别代表高维数组（张量）、自动求导（变量）和神经网络（层/模块），而且这三个抽象之间联系紧密，可以同时进行修改和操作。 简洁的设计带来的另外一个好处就是代码易于理解。PyTorch的源码只有TensorFlow的十分之一左右，更少的抽象、更直观的设计使得PyTorch的源码十分易于阅读。
- 速度
PyTorch 的灵活性不以速度为代价，在许多评测中，PyTorch 的速度表现胜过 TensorFlow和Keras 等框架。框架的运行速度和程序员的编码水平有极大关系，但同样的算法，使用PyTorch实现的那个更有可能快过用其他框架实现的。
- 易用
PyTorch 是所有的框架中面向对象设计的最优雅的一个。PyTorch的面向对象的接口设计来源于Torch，而Torch的接口设计以灵活易用而著称，Keras作者最初就是受Torch的启发才开发了Keras。PyTorch继承了Torch的衣钵，尤其是API的设计和模块的接口都与Torch高度一致。PyTorch的设计最符合人们的思维，它让用户尽可能地专注于实现自己的想法，即所思即所得，不需要考虑太多关于框架本身的束缚。
- 活跃的社区
PyTorch 提供了完整的文档，循序渐进的指南，作者亲自维护的论坛 供用户交流和求教问题。Facebook 人工智能研究院对 PyTorch 提供了强力支持，作为当今排名前三的深度学习研究机构，FAIR的支持足以确保PyTorch获得持续的开发更新，不至于像许多由个人开发的框架那样昙花一现。

## Pytorch 与 tensorflow 之间的差异在哪里？
PyTorch 最大优势是建立的神经网络是动态的, 对比静态的 Tensorflow, 它能更有效地处理一些问题, 比如说 RNN 变化时间长度的输出。各有各的优势和劣势。两者都是大公司发布的, Tensorflow（Google）宣称在分布式训练上下了很大的功夫, 那就默认 Tensorflow 在分布式训练上要超出 Pytorch（Facebook），还有tensorboard可视化工具, 但是 Tensorflow 的静态计算图使得在 RNN 上有一点点被动 (虽然它用其他途径解决了), 不过用 PyTorch 的时候, 会对这种动态的 RNN 有更好的理解。而且 Tensorflow 的高度工业化, 它的底层代码很难看懂， Pytorch 好那么一点点, 如果深入 PytorchAPI, 至少能比看 Tensorflow 多看懂一点点 Pytorch 的底层在干啥。

## Pytorch的常用工具包由哪些？

- torch ：类似 NumPy 的张量库，强 GPU 支持 
- torch.autograd ：基于 tape 的自动区别库，支持 torch 之中的所有可区分张量运行
- torch.nn ：为最大化灵活性未涉及、与 autograd 深度整合的神经网络库
- torch.optim：与 torch.nn 一起使用的优化包，包含 SGD、RMSProp、LBFGS、Adam 等标准优化方式
- torch.multiprocessing： python 多进程并发，进程之间 torch Tensors 的内存共享
- torch.utils：数据载入器。具有训练器和其他便利功能
- torch.legacy(.nn/.optim) ：处于向后兼容性考虑，从 Torch 移植来的 legacy 代码

## 环境安装
上面介绍完Pytorch的相关知识，接下来让我们进行环境安装。

现在PyTorch和Tensorflow不论是pip还是conda安装都能够直接自动绑定CUDA和CUDNN的安装，所以在开始运行本repo安装environment.yml中的包时已经安装过了，不必再专门自己去安装CUDA和CUDNN。但是，有些相对新一些的框架，比如JAX（可以参考这里），当需要GPU支持的时候，仍然需要自己手动安装CUDA和CUDNN。所以这里主要仍记录下CUDA和CUDNN的安装过程备查，最后也补充了下云服务器下的准备工作备用。

### Ubuntu 18.04

可以查看下自己的GPU是什么类型的。

$ sudo lshw -C display | grep product
product: GP102 [GeForce GTX 1080 Ti]

检查GPU的兼容性，官网上查看compute capability，满足大于3或者3.5的要求即可。

然后保证安装到Ubuntu上的包是最新的，因此

$ sudo apt update

$ sudo apt upgrade #will ask you Y/n if you want to upgrade

- 关于NVIDIA 的驱动：

Ubuntu预装了GPU的通用驱动。这些驱动不是优化的。因此需要找到适合自己的GPU的最新的NVIDIA驱动。有几种选择：

>- Nvidia PPA：非常好的选择。通过使用PPA中包含的驱动达到开箱即用的效果。
>- Ubuntu Default recommended driver：Ubuntu能指出自己的电脑需要的NVIDIA驱动
>- Nouveau：NVIDIA驱动的开源实现版本。
>- Official NVIDIA site：和PPA的一样，但是不会自动更新，并且有时在更新、卸载或者安装中会报错。

推荐的，也是比较好的方式是使用NVIDIA PPA来安装驱动。因为有最新的NVIDIA官方驱动，也在Ubuntu上测试过，且安装过程比较平滑。

$ sudo add-apt-repository ppa:graphics-drivers/ppa

$ sudo apt-get update

此语句将PPA库添加到Ubuntu的包系统内（Ubuntu是一种Debian Linux的发行版，因此使用的是Debian的dpkg包系统，该系统提供给Ubuntu应用来安装。高级包工具（APT）使得我们能很容易的在终端与dpkg交互）。

接下来需要决定安装哪个版本的driver。去PPA库网站上， 网页拉到最下面检查版本，发现很多版本都可以；也可以在官网上检查，官网会给出一个版本；

在命令行输入：

$ ubuntu-drivers devices

可以看到给出了几个版本的驱动。

显卡驱动对CUDA是向后兼容的，即安装了驱动后，使用命令nvidia-smi给出的CUDA版本是可以高于自己手动安装的CUDA的版本的，但是不能低，所以可以选择一个较新的稳定的驱动版本，这样PyTorch或Tensorflow自动安装CUDA的时候也没问题。

$ sudo apt install nvidia-driver-450

安装完毕之后需要重启电脑，直接命令行reboot即可，以使用新的显卡驱动：

$ sudo reboot

重启之后，在命令行键入：

$ nvidia-smi

查看是否已成功安装，出现一些信息基本上就是安装成功了。

自己在后续使用Ubuntu系统过程中可能会进行系统升级（apt-get upgrade），这可能会导致 Failed to initialize NVML: Driver/library version mismatch
这时候先重启下电脑就好了。

如果想要避免驱动自动升级，使用以下命令：

$ sudo apt-mark hold nvidia-driver-450
nvidia-driver-450 set on hold.

To reverse this operation run:

$ sudo apt-mark unhold nvidia-driver-450

- 安装CUDA

安装450驱动后，CUDA版本显示11.0，所以安装11.0及其之前版本的CUDA都是可以的。这里给的例子是CUDA 11.0
首先check下gcc和g++的版本。

$ gcc --version
gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0

$ g++ --version
g++ (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0

直接从官网下载，这里选择的是：这版

有提到要安装下kernel headers。（如果某个程序需要内核提供的一些功能，它就需要内核来编译程序，这个时候用的上kernel heads）。但几个也都没说。
```Python
$ sudo apt install linux-headers-$(uname -r)
```
执行命令即可安装，发现已经安装了。


根据下载网页上的提示，可以直接使用wget下载，然后直接安装：

$ wget https://developer.download.nvidia.com/compute/cuda/11.0.3/local_installers/cuda_11.0.3_450.51.06_linux.run

$ sudo sh cuda_11.0.3_450.51.06_linux.run

按照提示安装即可，注意因为之前已经安装过驱动了，所以这里提示问是否安装驱动时（Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 XXX.XX），选择no，其他的都可以选择yes或者默认值即可。

如果不是第一次安装cuda，即之前安装过旧版本的cuda，那么安装时会提示先删除之前的版本，就按照提示先删除之前的版本。

如果之前是通过 package manager安装 的，那么需要这么做来删除cuda工具（注意别删除nvidia驱动工具）：

$ sudo apt-get --purge remove "*cublas*" "cuda*" "nsight*" 

如果之前就是按照本教程选择的runfile安装的，参考这里来卸载（这里给的例子的链接是cuda10.1版本，如果是其他版本，查看对应的方法即可）:

$ sudo /usr/local/cuda-10.1/bin/cuda-uninstaller

清除完之前的版本之后，再重新进入安装包下载的文件夹，因为没有卸载nvidia驱动，而是直接安装的新的，所以如果还会提示有以前的安装包，那么参考这里，就执行下面语句安装:

$ sudo sh cuda_11.0.3_450.51.06_linux.run --toolkit --silent --override

安装之后检查cuda是否安装成功：

$ nvcc --version

然后配置环境变量。
```Python
$ sudo vim ~/.bashrc #打开配置文件并按i进入编辑模型，将以下信息写入
$ export PATH=/usr/local/cuda:$PATH

$ exportLD_LIBRARY_PATH=/usr/local/cuda/lib64:$\LD_LIBRARY_PATH

$ export CUDA_HOME=/usr/local/cuda

$ source ~/.bashrc
```
如果没有vim，安装即可，在命令行中输入：vim，没有安装的话会有提示，按照提示安装即可。

- 安装CUDNN

官网下载的对应cuda11.0版本的CUDNN。如果是第一次下载，需要首先注册一个NVIDIA的账号。
有下载tar压缩包和deb安装包两种方法，这里选择第一种，cudnn安装较容易，只需要把文件解压后拷贝进cuda根目录即可。
下载地址是这个：https://developer.nvidia.com/rdp/cudnn-archive#a-collapse805-110
选择的版本是 “cuDNN Library for Linux (x86_64)”
下载后，解压并进行相关配置：

$ tar -xzvf cudnn-11.0-linux-x64-v8.0.5.39.tgz

$ sudo cp cuda/include/cudnn.h /usr/local/cuda/include

$ sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64

$ sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

安装完成验证是否安装成功，参考[NV] How to check CUDA and cuDNN version：

$ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
Win10
这里安装cuda10.1及对应驱动，然后安装pytorch最新稳定版。首先如前所述，查看电脑的GPU是否足够支持pytorch和tensorflow： https://developer.nvidia.com/cuda-gpus#compute

比如我的笔记本GeForce 940M 5.0 是支持的。查看自己的电脑的显卡可以通过右键“计算机”文件夹，然后点击“设备管理器”，然后找到“显示适配器”即可看到。

然后查看自己可下载的NVIDIA Driver:https://www.nvidia.com/download/index.aspx?lang=en-us ，不过在下载安装之前，先看看cuda10.1对应的driver版本是什么：https://developer.nvidia.com/cuda-toolkit-archive

选择10.1版之后可以看到要下载的文件名里有cuda10.1对应的nvidia driver的版本，比如我选择的是10.1 update2：https://developer.nvidia.com/cuda-10.1-download-archive-update2?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal ，可以看到名称是cuda_10.1.243_426.00_win10.exe ，也就是说驱动版本是426
接下来就去这个网站：https://www.geforce.com/drivers 上找自己电脑对应的驱动版本，在manual driver search里面选择自己的显卡和操作系统信息，然后点击“START SEARCH”即可搜出匹配的driver版本。可以看到我的搜出来最老的也是440.97了，也和426不一致，所以还是选择直接从安装系统时就安装的nvidia软件里去更新了，参考网站：https://www.geforce.cn/whats-new/articles/nvidia-update

右键桌面，选择“NVIDIA 控制面板”，即可进入NVIDIA的界面。然而我的“帮助”栏下面并没有更新项目。所以最后放弃，直接安装最新的版本了。
如果安装顺利，那么就继续。

根据 CUDA10.1 安装文档：https://docs.nvidia.com/cuda/archive/10.1/cuda-installation-guide-microsoft-windows/index.html

安装需要vs的支持，可以看到cuda10.1支持vs2019 16.x 及之前版本，所以先安装一个vs2019.

然后接下来就可以安装cuda了。

然后是cudnn的安装。

云服务器安装
这里记录下Google Cloud Platform engine的使用。

一般个人电脑的GPU都不太好或者较旧，不太方便安装相应驱动来作计算，所以使用云端GPU是一个不错的选择，当然也可以远程连接到本地服务器上的GPU，这里主要记录远程使用Google GPU的方式，主要参考了：创建 PyTorch Deep Learning VM 实例，国内厂商云的可以参考:从0开始使用腾讯云GPU服务器，应该都大同小异。

为了使用GPU，首先要确保自己的项目有GPU资源，前提是先要有一个项目，云端项目管理可以参考：创建和管理项目，新建一个项目，我这里命名为'hydro-dl'

根据文档提示，首先访问“AI Platform Deep Learning VM Image Cloud Marketplace”页面，费用预估是一月300美元，可以先“启动”，回头再调整使用计费方式。点击之后可以看到刚刚创建的项目，选择hydro-dl，然后会提示需要创建结算账号，这样google才能收钱，就按照要求创建即可，这里结算账号我也命名为hydro-dl了，然后按顺序操作提交并启用结算功能即可，这时候再重新点击“启动”，然后选择hydro-dl项目，Google cloud就会配置Deep Learning VM了。

进入新的页面后，会提示GPU配额不足，需要现在配额页面增加配额，就根据提示前往配额页面，根据资源配额 页面介绍，用户需要首先申请调整配额，进入配额页面之后，过滤条件搜索NVIDIA，因为创建的时候提示的是NVIDIA Tesla K80，所以选择K80，然后就可以看到一系列服务，我就选择us-east-1，然后点击修改配额，输入个人信息以供联系，然后提交申请，需要等待google回复，回复的第一封邮件说需要2天，不过我这个申请比较小，所以几分钟就有回复了。然后配额完成还需要15分钟，所以稍等一会儿再重新进入Deep Learning VM 去部署，可以重新查看配额，还是搜索NVIDIA，选择K80，应该可以看到现在的 us-east-1 的那一条对应的限制已经是1了，说明修改完成，可以继续部署了。

很奇怪依然显示我的配额不足，那就暂时先不用这种“AI Platform Deep Learning VM Image Cloud Marketplace”的方式了，直接在compute engine上添加GPU来使用下看看到底是哪里有问题。

首先，首先，安装 gcloud命令行工具到最新版本，参考:gcloud compute。首先安装cloud SDK，按提示下载安装即可，需要等待一小段时间，最后完成时候，出现的选项应是全部默认勾选的，按默认的即可，这样可以进入命令行配置界面，提示需要登陆，选择Y，然后进入登陆网页，点击自己的google 账号，然后允许SDK权限申请即可使用Cloud SDK了。（不适用SDK也可以配置GPU）

接下来，完成一个虚拟机创建：添加或移除 GPU，Linux 虚拟机使用快速入门，前面已经完成了项目创建和结算启用，因为我已经启动了compute engine，所以这一步也不用再做了。

转到虚拟机实例页面，点击创建实例，设置实例名称为hydro-dl，要使用GPU，所以先确认下GPU在各地区的情况：Compute Engine 上的 GPU，各个GPU都有，所以默认的us-central1可以。默认的us-central1-a尝试了之后发现资源不足，创建不成功，所以选择us-central1-c。CPU我选择两个标准CPU 7.5G内存的，点击“CPU 平台和 GPU”标签，会显示添加GPU的选项。点击“添加GPU”，默认的K80即可。因为我更熟悉Ubuntu，所以将启动磁盘设置为Ubuntu，选择系统Ubuntu，然后版本选择18.04，磁盘也不贵，先选择300G用用。点击允许http流量，然后点击创建，发现提示配额不足，GPUS_ALL_REGIONS 有限制，说明需要的是GPUS_ALL_REGIONS的配额，所以还是需要重新去配，在配额界面搜索 GPUS_ALL_REGIONS，然后申请将限制改为1即可，再重新进入配额页面搜索，可以发现 GPUS_ALL_REGIONS 限制已经变为1了。现在按照前面的步骤重新创建实例，完成后即可得到一台远程的有GPU的机器了。不过好像直接创建还是不行，所以先等待15分钟，再试试。创建完成之后，就可以尝试远程连接了。

先不连接，因为如果自己去设置GPU驱动等还是有点麻烦的，所以现在重新回到“AI Platform Deep Learning VM Image Cloud Marketplace”页面，尝试直接使用deep learning VM。

现在进入页面，发现就没有配额限制的问题了。命名hydro-dl，地区还选择us-central1-c，然后framwork选择pytorch，勾选驱动安装以及jupyter，硬盘还选择300g，点击部署，等待即可，这会比之前部署的时候时间要久一些。生成之后进入到实例页面即可看到刚刚部署好的实例。

远程连接实例可以参考：连接到实例。在实例页面，点击SSH即可通过浏览器远程连接了。如果需要使用第三方工具，可以参考：使用第三方工具进行连接。这里使用mobaxterm尝试连接，参考了：How to connect to google cloud over Mobaxterm SSH以及Create Linux VM Instance on Google Cloud Platform & Access Via SSH From Windows

首先，在实例页面复制自己的google cloud的外部IP；

然后第三方工具都必须先生成自己的 SSH 密钥对，并将您的 SSH 公钥文件提供给实例，然后才能进行连接，所以这里第二步用 mobakeygen 工具来生成SSH key，选择tools峡的mobakeygen，然后点击generate，再随意移动自己的鼠标即可生成，生成后点击“save private key”,yes之后存入自己想放的位置，我命名了private_key；

然后copy自己的public key，在实例页面，选择左边栏的“元数据”，点击"SSH密钥"，点击“修改”，然后添加刚刚复制的公钥，并将最后的一串字符，我的是“rsa-key-20200727”改成自己的谷歌账号邮箱：xxx@gmail.com，然后保存即可；

接下来，再在云端使用ssh-keygen生成keygen，点击实例页面的"SSH"进入网页远程界面，在打开的界面输入 ssh-keygen，然后给文件命名，我命名为：google_cloud_ssh，密码直接两个回车跳过即可。然后命令行输入ls -la即可看到刚刚生成的ssh文件。copy google_cloud_ssh 到 .ssh/下：cp google_cloud_ssh .ssh/ ，然后进入.ssh文件夹输入ls可以看到copy进来的文件：先 cd .ssh ，然后 ls

最后就可以创建ssh连接了，点击session图标，然后选择SSH，在Remote host一栏写入：IP Address，即自己实例的外部IP，然后在Advanced SSH settings 里面导入刚刚保存的私钥，确定即可连接，然后输入用户名登陆，刚刚自己添加邮箱的时候的用户名：xxx@gmail.com里的xxx。即可进入页面。

如果没有用google提供好的镜像，久要自己安装nvidia驱动以及cuda，cudnn了，云端安装和本地略有不同，需要参考：安装 GPU 驱动程序。这里暂时没有尝试了。

连接到之后可以输入python, conda env list, nvidia等可以看到已经配置好的内容。接下来就可以尝试自己的项目了。
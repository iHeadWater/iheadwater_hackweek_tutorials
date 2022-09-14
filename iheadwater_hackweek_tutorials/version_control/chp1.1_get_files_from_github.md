# 获取文件

## 1. 仓库的目录结构

上述提到，**GitHub**的资源以仓库为单位。从本质上讲，仓库是一个特定项目的目录，它被**git**和**GitHub**认定为仓库，因为它包含一个名为` .git` 的子目录。

`.git` 子目录是自动创建的，如果是在 **GitHub.com** 上创建的，则由 **GitHub** 创建；如果是在电脑上先创建的仓库，则由 **git** 创建（即初始化为一个仓库）。这个 `.git` 子目录被这些工具用来管理和跟踪在这个目录上运行的各种任务（比如跟踪仓库中文件的变化）。因此，永远不需要访问或修改 `.git` 子目录中的文件。

除了 `.git` 子目录外，通常还有一些子目录用于工作流程的特定文件，如数据或脚本。大多数仓库中的几个常见文件：

1. `README.md`文件  : 这是一个`Markdown`文件，用来提供版本库的描述（即它的内容、目的等），以便其他人可以学习如何使用版本库中的文件。
2. `.gitignore`文件 : 这个文件可以用来列出不希望`git`跟踪的文件（即通过版本控制监控）。我们将在本章后面了解更多关于这两个有用的文件。

## 2. GitHub.com上仓库的URL

当一个仓库存储在**GitHub.com**上时，它会被分配一个唯一的**URL**（即GitHub.com网站上的链接），可以用来找到该仓库并访问其文件。**GitHub.com**上的仓库可以是公开的，也可以是私有的。

无论哪种情况（公开或私有），**GitHub** 仓库的 URL 链接总是遵循相同的格式：`https://github.com/username/repository-name`

用户名是该仓库创建者（即所有者）的用户名。这个用户名可以是个人，比如 `eastudent` （或者我们 **GitHub** 用户名），也可以代表一个组织，比如 `iheadwater_hackweek_tutorials`

例如，在这本教科书中我们将使用的资源库是由 `iheadwater_hackweek_tutorials` 所有，因此它的URL看起来像这样：`https://github.com/iheadwater_hackweek_tutorials/repository-name`

## 3. 在GitHub.com上创建其他用户的文件副本（Fork a Repo）

使用**GitHub.com**，我们可以复制一个由其他用户或组织拥有的**GitHub**仓库（也被称为 **repo**）,这项任务被称为**fork**仓库。其他用户也可以**fork**你的仓库，而原始仓库不会被修改。

被**fork**的仓库是与原始仓库是相连的。这意味着我们（或其他用户）可以将我们**fork**的仓库从原版更新到我们（或他们）的**fork**仓库。这也意味着我们可以对原始版本库提出修改建议，并由该版本库的所有者审核。因此，**fork**允许我们与他人协作，同时保护文件的原始版本。协作时，每个人都会用原始文件的副本工作。而且所有的修改都会在每个文件的历史中被跟踪，并可以在任何时候撤销。

可以从想复制的仓库的**GitHub.com**主页面**fork**一个现有的**GitHub**仓库。

fork仓库:

1. 导航到我们想分叉的版本库页面 - 例如。
`https://github.com/iheadwater_hackweek_tutorials
/practice-git-skillz`

2. 在仓库页面上，我们会看到右上角有一个按钮，上面写着Fork。该按钮旁边的数字告诉我们该 repo 已经被fork了多少次。
3. 点击 "fork"按钮，当它询问我们想在哪里fork该版本时，选择你的用户账户。
4. 一旦fork了该 repo，我们的账户中就会有一个副本。导航到我们的 repo 页面。网址应该是这样的：`https://github.com/your-user-name/practice-git-skillz`

要**fork**一个repo，首先导航到想**fork**的repo。然后点击屏幕右上角的**fork**按钮。然后就可以在我们的账户中创建一个该 repo 的副本。

![](../../../img/fork.jpg)

在这本教科书的后面，我们将学习如何对原始版本库提出修改建议，从原始版本库接收更新到我们的fork版本，并与他人合作。

## 4. 从GitHub.com复制文件到我们的电脑（git clone）

要在本地使用 **GitHub** 仓库（包括fork仓库），需要在电脑上创建该仓库的本地副本（这项任务被称为克隆仓库）。可以克隆自己的 **GitHub** 仓库，也可以克隆别人的仓库（比如我们fork到自己的 **GitHub** 账户的仓库）。

无论哪种情况，克隆都可以创建一个 **GitHub** 仓库的本地副本，这样就可以在本地电脑上处理文件了。克隆仓库是在本地处理文件的好方法，同时在云端的 **GitHub.com** 上还有一份文件副本。按照下面的步骤，我们将在**终端**使用 `git clone` 命令来克隆 **GitHub** 仓库。

### 4.1 使用Bash改变工作目录

使用任何 **git** 命令的第一步是将当前工作目录改为想要的目录。就 `git clone` 而言，当前工作目录需要是我们想下载 **GitHub** 仓库的本地副本的地方。

在这本教科书中，我们将克隆一个 repo 到你的电脑（或你工作的地方）上一个叫做 `iheadwater_hackweek_tutorials`的目录。这个 `iheadwater_hackweek_tutorials` 目录应该位于我们电脑的主目录中。

### 4.2 从GitHub.com复制一个Github.com仓库的URL

要运行 `git clone` 命令，我们需要想克隆的仓库的 URL（即拥有的仓库或从其他用户的仓库创建的fork）。

在该仓库的**GitHub.com**主页上，我们可以点击`Clone or download`的绿色按钮，然后把提供的URL复制到框中，看起来就像:`https://github.com/iHeadWater/iheadwater_hackweek_tutorials.git`

![](../../../img/https.jpg)

也可以根据SSH钥匙，来复制仓库（可将SSH钥匙理解成远程连接本地电脑的一把钥匙），然后把提供的SSH复制到框中，看起来就`git@github.com:iHeadWater/iheadwater_hackweek_tutorials.git`

![](../../../img/ssh.jpg)

### 4.3 在终端运行 Git 克隆命令

现在有了想复制到本地的版本库的URL，可以用终端运行`git clone`命令，后面跟上复制的URL或者SSH:`git clone https://github.com/iHeadWater/iheadwater_hackweek_tutorials.git`、`git clone git@github.com:iHeadWater/iheadwater_hackweek_tutorials.git`

**注：** SSH密钥是需要配置的，下一节会讲如何配置

现在已经在 `iheadwater_hackweek_tutorials` 目录下做了一个版本库的本地拷贝。可以用**终端**的`ls`命令仔细检查这个目录是否存在。
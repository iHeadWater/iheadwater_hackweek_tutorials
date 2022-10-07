# 使用VSCode编写运行代码

上一节在jupyter上运行的代码最初就是在vscode上调试编写的，因为相比于jupyter，vscode这类IDE更适合编写、调试代码，jupyter还是更多地是帮助我们做数据分析，或者是快速验证一些程序。

本节就重点介绍，如何使用vscode连接平台计算资源，编辑运行代码。

当然你也可以直接在本地运行你的代码，你也可以试试你自己平常习惯用的其他IDE，这里选择vscode是因为vscode能通过插件支持多种语言，这样我们就不必针对每种语言再专门写文档介绍了。

以下步骤第一次做会觉得有点麻烦，但是它是一次性的，以后带给你的方便会让你觉得值得的。

## 1 下载安装配置VSCode

首先在本地设置好vscode，你就能在本地用它了，不过本节重点讨论远程连接到平台。

### 1.1 本地下载安装vscode

首先，要在你自己的电脑（本地）上下载安装vscode软件，直接在[vscode官网](https://code.visualstudio.com/)下载，然后一路默认安装即可。

![](../img/vscode_download.png)

### 1.2 登录以同步设置

打开vscode，点击vscode窗口左下角的账户或设置按钮，选择“登录以同步设置”，这样后面你的设置就可以在多个地方同步，而不用换一台电脑就要重新配置一遍。

![](../img/vscode_login.png)

vscode上方会弹窗让用户选择采用Microsoft还是Github登录，若选前者，浏览器会跳出MS账户登录页面，若选后者，vscode会在浏览器中打开一个GitHub校验标签页，不必管它，连接成功后浏览器会自动跳回vscode。

如果你跟着前面的教程做到这里，那你应该注册过GitHub账号了，所以直接用它就好了。

此时设置同步便已启用：

![](../img/vscode_sync_opened.png)

你什么都不用做，下次换台电脑再安装vscode，登录后，会自动同步好你的所有配置。

### 1.3 安装Python相关插件

插件窗口下搜索 Python，排名第一的插件下载下来：

![](../img/vscode_plugin_python.png)

类似的操作，建议把下面这些插件都安装好：

- [汉化](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)
- [智能补全](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- [Markdown](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Python代码检查错误](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python代码注释](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

### 1.4 Optional: Java相关插件

尽管我们不鼓励使用Java进行科研编程，但考虑到以往一些历史科研代码是用Java编写的，所以这里仍然给出Java的相关说明。

让我们先本地安装一个JDK，来测试接下来安装的Java插件是不是好用。

从[openjdk官网](https://jdk.java.net/archive/)下载OpenJDK17（为什么是JDK17？因为它是目前最新的Java长期支持版本）。

![](../img/openjdk_download.png)

解压后就能用了，把解压后的文件夹放到你想放的任意位置，但是后面这个位置不能随便改了。

然后我们配置环境变量：在系统环境变量内新建名为JAVA_HOME的变量，并将其变量值指定为JDK安装位置（vscode需要JAVA_HOME环境变量确定JDK位置）

![](../img/env_var.png)

![](../img/env_var_javahome.png)

然后在VSCode下面安装 [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) 插件，这个插件会安装一系列VSCode下进行Java代码开发的必备插件。

![](../img/vscode_java_plugin.png)

然后会引导我们进入一个开始Java开发的教程界面，按照里面的操作做一遍，就知道VSCode下如何开展Java开发了（仔细阅读它提供的教程的全部内容）。

![](../img/vscode_java_tutorial.png)

比如这是本地运行hello world的情况：

![](../img/vscode_run_java.png)

## 2 使用VSCode连接平台

下面看看远程连接平台。

### 2.1 安装远程连接插件

选择左侧Extensions 选项卡，在输入框搜索 remote ，选择安装Remote-SSH插件。

![](../img/vscode_install_plugin.png)

安装完成之后会在左侧新增一个选项卡Remote Explorer，如下图所示

![](../img/vscode_remote_plugin.png)

### 2.2 确认本地电脑已连接个人平台账号

如果前面已经使用过[Mobaxterm上传下载了文件](https://iheadwater.github.io/iheadwater_hackweek_tutorials/chp2_file_formats/chp2.4_your_data.html#id2)，那么您现在正在使用的电脑应该就已经连接到您个人的平台账号了，即您的本地电脑是客户端，个人平台账号是服务端，两者之间已经建立起SSH连接了。

如果没有请查看[Mobaxterm上传下载文件](https://iheadwater.github.io/iheadwater_hackweek_tutorials/chp2_file_formats/chp2.4_your_data.html#id2)这一节，配置本地客户端和个人平台服务端之间的SSH连接。

### 2.3 添加远程服务器连接配置

点击该选项卡，会进入SSH TARGETS的添加，如下图所示，点击设置按钮，vscode会弹框询问选择哪个配置文件，一般只需选择最上面的文件（C:\Users\你的用户名\.ssh\config）：

![](../img/vscode_ssh_setting.png)

进入配置文件后，复制粘贴如下文本：

```Plain Text
Host jupyterhub.waterism.com
    HostName jupyterhub.waterism.com
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey
    User 你在平台jupyterhub上注册的账号名
```

然后保存即可。

### 2.4 连接平台

如无意外，SSH Targets中会生成一个jupyterhub.waterism.com项（和你粘贴进去的Host一致），鼠标右键点击此项，选择在“当前窗口”或者“新建窗口”打开，两个选项选择任意一个即可。

![](../img/vscode_ssh_connect.png)

remote ssh插件便会为你自动连上jupyter服务器，连接成功后，窗口左下角远程小窗口会出现jupyterhub.waterism.com字样：

![](../img/vscode_ssh_login.png)

此刻便已连接成功。

选择“文件”-> “打开文件夹”：

![](../img/vscode_ssh_opendir.png)

选择一个文件夹打开即可。

:::{note}
注意：若用户在外网连接内部服务器失败，报错Time out，请注意是否已经打开研发中心的VPN。
:::

注意一下vscode插件窗口，尤其是SSH远程服务器部分：

![](../img/vscode_ssh_plugin.png)

和“本地-已安装”是分开的两个部分。

如果刚刚本地安装了很多插件，这时候远程也会提示你安装相同的插件，安装即可。

### 2.5 运行代码

如果您之前跟着一起实践了git和github部分的操作，那么这里应该已经有一些代码在服务器上了。

这里以本教程的代码为例，如果已经在服务器上下载过，直接打开 iheadwater_hackweek_tutorials 代码文件夹即可

然后，选择Python的解释器：按快捷键 “ctrl+shift+p”，输入 python: select interpreter，选择它，然后选择 平台上已经提供的 tutorial 环境，就为iheadwater_hackweek_tutorials 配置好运行环境了。

现在我们就可以运行代码了。比如打开iheadwater_hackweek_tutorials/lstm_camels/lstm_camels.py 文件，直接运行即可：

![](../img/vscode_ssh_runpython.png)

你会得到和上一节jupyter上运行同样的结果。

Optinal:Java代码的远程运行是类似的，只要你在平台服务器上有java项目，通过SSH连接后，打开它，然后在插件栏中的远程部分安装好[Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) 插件，就能运行你的java代码了。

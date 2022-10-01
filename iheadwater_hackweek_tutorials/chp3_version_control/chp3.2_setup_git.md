# 配置Git

之前学过如何`fork` **GitHub** 仓库以复制其他用户的仓库，也学过如何下载 **GitHub** 仓库的副本（即`clone`）到电脑上。在这一页，我们将学习如何在电脑上设置**git**。下面我们一起来看一下如何操作吧！

## 1. 在电脑上配置git用户名和电子邮件

第一次在电脑上使用 **git** 时，需要给 **git** 配置用户名和电子邮件地址，这些信息将被用来记录谁对 **git** 中的文件进行了修改。配置的时候，我们最好使用**GitHub.com**上设置的电子邮件地址和用户名。

首先，可以在**终端**上输入**Github.com**的用户名来设置。

`$ git config --global user.name "username"`

接下来，可以通过键入来设置你的**Github.com**账户的电子邮件。

`$ git config --global user.email "email@email.com"`

在这里需要注意一些东西，如果使用了`--global`配置选项，那么该命令只需运行一次，之后无论你在该系统上做任何事情，**git** 都会使用那些信息。

最后，可以用以下命令检查对`user.name`和`user.email`的配置。

`git config user.name`，它返回之前设置的用户名

`git config user.email` 会返回之前设置的电子邮件。

这些设置可以确保对仓库所做的修改归于我们的用户名和电子邮件。

## 2. 通过GitHub为Git设置身份验证

GitHub 要求通过认证才能对 repo 进行任何修改。有两种方法来设置GitHub的认证。

1. 使用个人访问标识，可以在GitHub.com上设置并在本地使用该标识进行认证。这涉及到在GitHub.com上创建一个标识，然后在本地bash中使用它作为 "密码"。
2. 使用SSH：这需要在本地进行更多的设置，但一旦设置好了，你就可以跳过每次对 repo 进行修改时的认证步骤。

### 2.1 建立与GitHub的SSH连接（推荐）

SSH是Secure SHell的缩写，是一种从电脑上认证GitHub的替代方式。SSH一旦设置好，就不必再去验证与GitHub的连接。这是因为电脑上会有一个储存在本地的密钥，可以与储存在 GitHub 账户中的密钥进行验证。

首先，使用如下命令创建密钥文件：
```Python
ssh-keygen -t rsa -C 你的github账号邮箱
```

输入后会提示保存key的文件以及passphrase，选择直接回车（一共三次），保存到默认位置，默认设置即可。

然后命令行上会显示处出密钥保存路径，其中私钥文件是 id_rsa，公钥文件是 id_rsa.pub

然后需要将SSH公钥添加到自己的GitHub账户。

- 复制id_rsa.pub文件中的全部内容
- 登陆到GitHub上，右上角小头像->Setting->SSH and GPG keys中，点击new SSH key，将复制的所有内容添加到其中；名称可以随便起

接下来测试链接：

```Python
ssh -T git@github.com
```

将会看到如下提示：

The authenticity of host 'github.com (xxx.xxx.xxx.xxx)' can't be established. RSA key fingerprint is xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Are you sure you want to continue connecting (yes/no)?

输入yes，然后回车即可，这时候结果为 “ …You’ve successfully authenticated, but GitHub does not provide shell access”，则说明成功。

https下下载的方式和ssh下一样，在github中clone时选择HTTPS即可，比如下载本repo：

```Python
git clone https://github.com/iHeadWater/iheadwater_hackweek_tutorials.git
```

如果已经使用了https，想要切换成ssh 变化远程仓库地址 可以按照下面方式操作（参考了这里）。

先使用下面语句查看一下远程仓库

```Python
git remote -v
```

如果之前是直接使用https下载的repo，那么应该可以看到origin后面是“https:...”，现在切换:

```Python
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git  
```

再次执行`git remote -v`查看远程仓库，可以看到发生了变化。

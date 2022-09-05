# iHeadWater Hackweek Tutorials

水资源科研编程入门教程，网页在这里：https://iheadwater.github.io/iheadwater_hackweek_tutorials

## 一起编辑本书

如果你想一起编辑本书:

1. 克隆本代码库
2. 运行 `pip install -r requirements.txt`（推荐在虚拟环境中）
3. 编辑`iheadwater_hackweek_tutorials/`文件夹中的源文件（怎么编辑内容请参考[jupyterbook的文档](https://jupyterbook.org/en/stable/start/new-file.html)）
4. 运行 `jupyter-book clean iheadwater_hackweek_tutorials/` 来删除之前构建的文件
5. 运行 `jupyter-book build iheadwater_hackweek_tutorials/`

然后本书的HTML版本就会被构建在`iheadwater_hackweek_tutorials/_build/html/`文件夹中，你可以在浏览器中打开先看看自己编写的内容，推送更新时不需要将build文件夹下的内容推送上去。

## 发布本书

本书借助了cookiecutter模板[cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book)的持续集成工具，能直接将本书内容发布到GitHub Pages上。发布的方式可以参考[jupyterbook的文档](https://jupyterbook.org/en/stable/start/publish.html)

如果你想让你撰写的内容也展示在网页上，推送你的分支到本代码仓即可，后续我们会合并并发布到网上。

我们会将文件推送到github本仓的main分支，之后有自动化程序会创建代码运行环境，build代码，并将生成的文件推送到gh-pages分支上等，然后网页就会自动显示刚推送的内容了。

## 本书作者

欢迎大家积极贡献，这里是目前的贡献者：[contributors tab](https://github.com/iHeadWater/iheadwater_hackweek_tutorials/graphs/contributors)

## 致谢

本书使用了开源工具 [Jupyter Book project](https://jupyterbook.org/) 和 [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book)，感谢开源社区的贡献者们。

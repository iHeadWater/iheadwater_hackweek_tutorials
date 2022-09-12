# Jupyter Hub/Lab/Notebook 简介

Jupyter 是一个开源平台，其中包含一套工具，包括：

- Jupyter Notebook：一个基于浏览器的应用程序，可以创建和共享包含实时代码、方程式、可视化和叙述性文本的文档（即 Jupyter Notebook 文件）
- Jupyter Lab：一个基于浏览器的应用程序，可以访问多个 Jupyter Notebook 文件以及其他代码和数据文件
- Jupyter Hub：可以在服务器上运行的多人版 Jupyter Notebook and Lab

我们用的是Lab，写的是Notebook，Hub支持多人使用Lab。

## Ⅰ. 什么是Jupyter NoteBook？

简单讲，Jupyter Notebook就是一个集成开发环境 (IDE)，允许我们编写代码、导航文件、检查变量等。

## Ⅱ. 开放可重复性的Jupyter Notebook

Jupyter Notebook 文件格式 ( .ipynb) 将描述性文本、代码块和代码输出组合在一个文件中。我们运行代码时，它会在笔记本文件中生成输出，包括绘图和表格。然后，可以将笔记本导出到一个.pdf或.html然后可以与任何人共享。

这种格式很强大，我们可以：

1. 与可能想要运行它的任何人共享笔记本本身
2. 将笔记本转换为可以像报告一样查看的 PDF 或 HTML 格式
3. 使用 Jupyter Notebooks（.ipynb文件）来记录工作流程并共享代码以进行数据处理、分析和可视化。

## Ⅲ. Jupyter Notebook的组件

- **Environment** : 环境是你编写和运行代码必备的条件！环境中包含很多依赖包。拿**Python**语言编写代码为例，我们用`Numpy`依赖包储存和处理大型矩阵、用`Matplotlib`依赖包进行2D绘图实现结果的可视化（用图来表示结果，如此更形象）等等

![](../../../img/依赖包.jpg)

- **.ipynb**  : 笔记本的文件类型，是编写 `Code` 与`Markdown` 的地方，也就是我们实际操作的地方
- **Kernels** ： 一个内核以一种特定的编程语言运行代码。`Jupyter Notebook`支持超过40种不同的语言。

### 1. 笔记本的结构

- Menu bar
- Toolbar
- Cells

### 2. 笔记本中的 Markdown 和 Code

`cells`用来存储文档文本，如`Markdown`或编程代码，如**Python**。

使用`Markdown`语法编写的文本可以在属于`Markdown`类型的单元格中呈现，代码是以代码块的形式编写的，我们可以在`Jupyter Notebooks` 中结合 `Markdown`和 `Code` 来记录工作流程

下一节中，我们将学习如何运行`cells`，并向我们的`Jupyter Notebook`文件添加新的单元，以建立工作流程。

## 使用 .ipynb 

打开`Jupyter Hub`，在`Notebook`下选着一个**Python**内核，即可创建一个`.ipynb`

我们看`Notebook`下的一个**Python**内核，例如`Python(gis-base)`。内核是**Python**，括号里的`gis-base`是环境。内核只是选择了一门语言，而不管用哪种语言编程，都需要依赖包支持。`gis-base`环境下就存储了很多`Gis`相关的依赖包。

现在打开`.ipynb`，会出现一个矩形单元格，在此矩形单元格中可以进行 `Code` 或 `Markdown` 编写，在上方可为此单元格选择是 `Code` 模块还是 `Markdown` 模块

**创建新单元格**

快捷键如下：

`create new cell : Esc+a(above),Esc+b(below)`
`Copy Cell : c`
`Paste Cell ： v`

新单元格的默认类型是代码，但我们可以通过点击单元格并在工具栏的单元格类型菜单中选择一个新的单元格类型（如`Markdown`）来改变任何现有单元格的类型。

单元格类型选项包括代码、`Markdown`、`Raw NBConvert`（用于保持未被`nbconvert`修改的文本）和`Heading`。

要使用键盘快捷键，请按下`esc`键。之后，通过点击`m`键将一个单元格改为`Markdown`，或者通过点击`y`键将一个单元格改为`Code`。

接下来就开始创建一个单元格
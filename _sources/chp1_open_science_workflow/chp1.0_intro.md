# 编程概念及相关工具

在本书的第一部分开始前，我们首先探讨一个问题，即编程或者计算机技术在水资源相关专业中能发挥什么作用？

先看看和我们专业相关的一些文献中是怎么说的 {cite}`open_science_2021,hess-26-647-2022,hess-23-2939-2019`。

Clark等指出：

> data/model availability is a requirement to publish in AGU journals. The **FAIR initiative** (data/models should be Findable, Accessible, Interoperable, and Reusable) arguably reduces duplication of effort, and can help to accelerate progress on key problems in hydrology and other sciences

Hall等则说：

> Hydrologic research often relies on the use of computational models and research software, which must be archived with appropriate documentation and publicly accessible for **verifiability and reproducibility** of results

Slater等提到：

> True **reproducibility** requires more than the mere repeatability of results with the same computer code and data: one must also be able to reproduce a study’s conclusions when testing the theory with different data or a different model set-up

他们都提到了可复现，我们都知道科研成果如果不能被复现就可以被怀疑不真实，所以可以复现这点是非常重要的。另外，他们也提到了数据和模型的可获取对科研十分重要，毕竟如果数据和模型我们都获取不到，想要复现相关科研成果也是不可能的。

那么编程对于这些又有什么意义呢？

编程能帮助我们**自动执行一系列任务**，包括模型算法的一系列内容以及执行模型算法涉及到的各类型准备工作，这有助于快速复现科研工作。相比之下，基于图形用户界面 （GUI） 的工作通常需要交互式手动步骤进行处理，这些工作其实是很难复现的，因为记录他们都不是一件容易事，尤其是步骤特别多的时候。另外，如果使用的GUI工具还是需要许可证的，那么没有资源购买该工具的人员将就无法复现同样的工作，有些人会使用盗版工具，从小了来说，是破坏知识产权的不良行为，从大了说，在损伤我们的自主研发能力。这与大力倡导自主研发和产业升级的时代背景是不相符的。

那么为了可复现的科学研究，我们需要了解掌握什么样的编程工具和编程技术呢，这就是本教程的主要目的之一了。本教程最终有一个主线目标，就是大家一起尝试复现近期一些论文中的计算结果，在复现这个的过程中我们来达成刚刚提到的目的。

本章首先让我们来初步认识可复现科研的一般工作流程并掌握这一过程中常用的一些基本工具，主要包括计算机的终端、版本控制工具和编程编辑器等，看完本章你将：

1. 知道可复现科研一般工作流是什么样的
2. 会在终端中运行命令以处理计算机上的文件和目录。  
3. 初步了解版本控制工具Git和相关的Github
4. 能简单使用jupyterhub提供的工具

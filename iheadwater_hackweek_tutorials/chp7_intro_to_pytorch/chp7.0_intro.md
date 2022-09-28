# 初探Pytorch

## 什么是Pytorch？

Pytorch是torch的python版本，是由Facebook开源的神经网络框架，专门针对 GPU 加速的深度神经网络（DNN）编程。Torch 是一个经典的对多维矩阵数据进行操作的张量（tensor ）库，在机器学习和其他数学密集型应用有广泛应用。但由于Torch语言采用 Lua，导致在国内一直很小众，并逐渐被支持 Python 的 Tensorflow 抢走用户。作为经典机器学习库Torch 的端口，PyTorch 为 Python 语言使用者提供了舒适的写代码选择。

## 为什么选择Pytorch？

目前常用的深度学习库，tensorflow、keras 和 pytorch。。。

- 简洁：
PyTorch的设计追求最少的封装，尽量避免重复造轮子。不像 TensorFlow 中充斥着session、graph、operation、name_scope、variable、tensor、layer等全新的概念，PyTorch 的设计遵循tensor→nn.Module 两个由低到高的抽象层次，分别代表高维数组（张量）、和神经网络（层/模块），而且这三个抽象之间联系紧密，可以同时进行修改和操作。 简洁的设计带来的另外一个好处就是代码易于理解。PyTorch的源码只有TensorFlow的十分之一左右，更少的抽象、更直观的设计使得PyTorch的源码十分易于阅读。
- 易用：
PyTorch 是所有的框架中面向对象设计的最优雅的一个。PyTorch的面向对象的接口设计来源于Torch，而Torch的接口设计以灵活易用而著称，Keras作者最初就是受Torch的启发才开发了Keras。PyTorch继承了Torch的衣钵，尤其是API的设计和模块的接口都与Torch高度一致。PyTorch的设计最符合人们的思维，它让用户尽可能地专注于实现自己的想法，即所思即所得，不需要考虑太多关于框架本身的束缚。
- 速度：
PyTorch 的灵活性不以速度为代价，在许多评测中，PyTorch 的速度表现胜过 TensorFlow 和 Keras 等框架。框架的运行速度和程序员的编码水平有极大关系，但同样的算法，使用PyTorch实现的那个更有可能快过用其他框架实现的。
- 活跃的社区：
PyTorch 提供了完整的[文档](https://pytorch.org/tutorials/)，循序渐进的指南，作者亲自维护的论坛 供用户交流和求教问题。Facebook 人工智能研究院对 PyTorch 提供了强力支持，作为当今排名前三的深度学习研究机构，FAIR的支持足以确保PyTorch获得持续的开发更新，不至于像许多由个人开发的框架那样昙花一现。
- 更适合科研编程：
PyTorch 最大优势是建立的神经网络是动态的, 对比静态的 Tensorflow, 它能更有效地处理一些问题, 比如说 RNN 变化时间长度的输出。各有各的优势和劣势。两者都是大公司发布的, Tensorflow（Google）宣称在分布式训练上下了很大的功夫, 那就默认 Tensorflow 在分布式训练上要超出 Pytorch（Facebook），还有tensorboard可视化工具, 但是 Tensorflow 的静态计算图使得在 RNN 上有一点点被动 (虽然它用其他途径解决了), 不过用 PyTorch 的时候, 会对这种动态的 RNN 有更好的理解。而且 Tensorflow 的高度工业化, 它的底层代码很难看懂， Pytorch 好那么一点点, 如果深入 PytorchAPI, 至少能比看 Tensorflow 多看懂一点点 Pytorch 的底层在干啥。

## Pytorch的常用工具包由哪些？

- torch.nn ：神经网络
- dataset和dataloader：加载训练、测试数据

。。。。
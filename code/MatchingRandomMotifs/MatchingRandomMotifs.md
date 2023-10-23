## [Matching Random Motifs](https://rosalind.info/problems/rstr)

### 背景知识

这个问题的任务是计算一个功能模块(motif)，或者一个已知的启动子在一个随机构建的基因组中出现的概率。这个问题的难点是，无法真实构建长基因组，而是
建立一个与功能模块长度相同的小的随机字符串的集合。这些字符串代表了基因组的子串，可以用于对功能模块的概率进行估算。

**对立事件**: 对于一个随机事件A和另一个随机事件B，若A交B为不可能事件，A并B为必然事件，那么称A事件与事件B互为对立事件，其含义是：事件A和事件B必
有一个且仅有一个发生。

### 问题

给定：给定一个正整数N<=100000，一个小数x(在0,1之间)，以及一个DNA序列s(10bp左右)

如：9000 0.6 ATAGCCGA

输出：N个与s等长且GC含量为x的随机DNA序列,至少有一个和s相同的概率。

如：0.689

### 解决

首先求一个随机序列与s相同的概率

<a href="https://latex.codecogs.com" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(s)%20=%20\sum%20P(s_{i})" /></a>

然后，不相同的概率是1-P(s), N个序列都不相同的概率为

<a href="https://latex.codecogs.com" target="_blank"><img src="https://latex.codecogs.com/gif.image?\dpi{110}P_{N}=(1-P(s))^{N}" /></a>

至少有一个和s相同的概率即为PN的逆事件

<a href="https://latex.codecogs.com" target="_blank"><img src="https://latex.codecogs.com/gif.image?\dpi{110}P=1-P_{N}=1-(1-P(s))^{N}" /></a>


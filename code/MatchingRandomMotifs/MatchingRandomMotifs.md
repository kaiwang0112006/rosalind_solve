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

### 扩展

在[Introduction to Random Strings](https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/IntroductiontoRandomStrings/IntroductiontoRandomStrings.md)
中，我们讨论了在基因组中寻找功能模块的问题。功能模块的出现可能是随机发生的，我们的目标就是量化随机的概率值。

我们关心的功能模块是启动子，或者说基因转录的DNA起始序列。启动子通常是位于基因的起始区域的短序列，包含与RNA聚合酶的初始结合位点，是转录的起点。
寻找启动子通常是基因预测的第二步，第一步是建立开放阅读框([Open Reading Frames, ORF](https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/OpenReadingFrames/OpenReadingFrames.md))

识别启动子并没有快捷的方法。在大肠杆菌中，启动子包含两种序列:TATAAT和TTGACA。通常位于基因的ORF的上游10或者35个碱基。而这两种启动子序列也是共有序列
(consensus strings)。在大多数启动子中也能部分发现两种序列。细菌的启动子可能还包含其他区域，可与特异性的蛋白结合或改变转录的强度。

真核生物的启动子更加难于识别。大多数情况有一个TATA框(TATA box)。TATA box又称为基本启动子(basal promoter)，它与上游的TFIIB识别元件
(TFIIB recognition element,BRE)，以转录起始位点为中心的起始子(initiator, Inr)，以及下游启动子元件(downstream promoter element, DPE)
一起构成核心启动子，其它均称为上游元件。TATA box和BRE通常位于转录起始的40bp以内。就此而言，真核生物的基因可以在上游几千bp远找到大量有调节功能
的启动子。
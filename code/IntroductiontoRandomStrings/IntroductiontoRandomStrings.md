## [Introduction to Random Strings](https://rosalind.info/problems/prob/)

### 背景知识

**1. 数组 (Array)**

**2. 随机字符串 (Random String)**

随机字符串字符串中每个字母都按照字母的概率概率分布随机抽取。比如按照一个固定的GC占比生成的随机DNA序列，如果GC占比是x，C和G的概率分别为x/2，A和T的概率
分别为(1-x)/2。

**3. 自然对数概率 **

实际中，很多概率计算结果会非常小，通常会取概率的以10为底的对数

### 问题

给定：一个DNA序列长度为100bp，以及一个数组长度约20，包含一组GC占比

输出：数组B长度与A相同。B[k]代表按照A[k]的GC占比生成随机序列s的概率

### 解决

基于对数可加性可以直接计算P(s)=B[k]是s的每个碱基字符分布概率乘积，即:

<a href="https://latex.codecogs.com" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(s)%20=%20\sum%20P(s_{i})" /></a>

其中

<a href="https://latex.codecogs.com" target="_blank"><img src="https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/IntroductiontoRandomStrings/form1.gif" /></a>

即

    def main():
        with open(r"rosalind_prob.txt") as f:
            data = f.readlines()
        seq = data[0].strip()
        problist = [float(i) for i in  data[1].split()]
        print(seq)
        print(problist)
        probRecord = []
        for i, p in enumerate(problist):
            logarithm = 0
            probmap = {}
            probmap["A"] = (1 - problist[i]) / 2
            probmap["T"] = (1 - problist[i]) / 2
            probmap["C"] = problist[i] / 2
            probmap["G"] = problist[i] / 2
            for s in seq:
                s = s.upper()
                logarithm += math.log(probmap[s],10)
            probRecord.append(str(logarithm))
        print(" ".join(probRecord))

### 扩展

基因组不是一个随机的字符串，我们已经知道motif的概念 ([Finding a Motif in DNA](https://rosalind.info/problems/subs/))。如果一个motif
在多个物种中存在，那么很大可能是一个重要的功能模块。但是像人的基因组又32亿的碱基对，所以在分析基因的时候需要区分有些motif是随机出现的。




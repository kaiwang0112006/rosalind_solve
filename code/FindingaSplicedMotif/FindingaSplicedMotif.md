## [Finding a Spliced Motif](https://rosalind.info/problems/sseq/)

### 背景知识

**1. 子字符串和下标**

子字符串是指由一个长字符串的字符组成的短字符串，且字符在短字符串中的下标排序和在长字符串中一样。

### 问题

给定：两个DNA序列s和t

输出：t作为s的子字符串在s中的下标列表，（不唯一的情况下只输出一个）

### 解决
    s = 
    t = 
    indmap = []
    for i, ti in enumerate(t):
        if i == 0:
            indmap.append([m.start()+1 for m in re.finditer(ti, s)])
        else:
            indmap.append([m.start() + 1 for m in re.finditer(ti, s) if m.start() + 1>min(indmap[i-1])])

    for prod in product(*indmap):
        if tuple(prod) == tuple(sorted(prod)):
            print(" ".join([str(i) for i in prod]))
            break

### 扩展

在之前([“Finding a Motif in DNA”](https://rosalind.info/problems/subs/)), 曾经尝试在基因序列中以子字符串的方式查找motif。但是， DNA
序列常常被内含子分隔成段。所以，这一节就是试图识别被内含子分开的motif序列。
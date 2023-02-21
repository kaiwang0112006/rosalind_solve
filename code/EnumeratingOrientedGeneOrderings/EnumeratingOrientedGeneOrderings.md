## [Enumerating Oriented Gene Orderings](https://rosalind.info/problems/sign/)

### 背景知识

**1. 符号置换组合 (signed permutation)**

一个正整数n的符号置换组合是指在正整数组成的集合{1,2,...,n}中的元素符合随机为正号或者负号。比如π=(5,−3,−2,1,4)是正整数5的一个符号置换组合。

### 问题

给定：一个正整数n<=6

输出：长度是n的所有符号置换组合总数，以及每个符号置换组合。

### 解决

    from itertools import *
    import copy
    def main():
        n = 2
        dlist = []
        for prod in (product(*[(-i, i) for i in p]) for p in permutations(range(1, n + 1))):
            for perm in prod:
                dlist.append([str(j) for j in perm])
        print(len(dlist))
        for d in dlist:
            print(" ".join(d))

### 扩展

两个物种的基因组中相似的区域称为同义基因块(synteny blocks)，这往往是由于重排序导致的翻转和移位造成的。然而DNA单链是有方向的，RNA转录只在一个方向上
发生。因此为了更好的找到同义基因块，我们需要给每个基因块一个方向。
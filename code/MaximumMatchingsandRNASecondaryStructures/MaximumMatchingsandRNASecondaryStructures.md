## [Maximum Matchings and RNA Secondary Structures](https://rosalind.info/problems/mmch/)

### 背景知识

在[Perfect Matchings and RNA Secondary Structures](https://rosalind.info/problems/pmch/)中，我们假设RNA序列中A和U的数量
相等，C和G的数量相等，计算了完美匹配的数量。而当AUCG的数量不相等的时候，就无法构造完全匹配。

<img src="https://rosalind.info/media/problems/mmch/maximum_matching.png" title="maximum_matching"/>

因此定义了最大匹配(Maximum Matchings)，即一个图中包含最多边的匹配。而RNA序列的连接图中的最大匹配就是尽可能多的形成碱基对。

<img src="https://rosalind.info/media/problems/mmch/unbalanced_bonding_graph.png" title="bonding_graph"/>

### 问题

给定：给定一个RNA序列长度约100bp

输出：可以得到的最大匹配的数量

### 解决

和[Perfect Matchings and RNA Secondary Structures](https://rosalind.info/problems/pmch/)解决思路类似，只不过这次我们要考虑AU(或者CG)的数量不一致，因此阶乘要除以碱基差。

    def main():
        seq = "AAAGGCUUGGAUUGUCAUACUUGUUAAGGCAUCGUAGGCGGCAGUCCGGAAGGUAACGAACUGGUCGAGGACGUACUCCCAGAGUGGAGAU"

        A = seq.count('A')
        U = seq.count('U')
        C = seq.count('C')
        G = seq.count('G')

        GCmax = max(G, C)
        GCmin = min(G, C)
        AUmax = max(A, U)
        AUmin = min(A, U) # 把每一对中较大的和较小的分出来

        if min(A,U,C,G) == 0:
            num = 0
        else:
            MMAU = factorial(AUmax)//factorial(AUmax-AUmin)
            MMGC = factorial(GCmax)//factorial(GCmax-GCmin)
            num = MMAU*MMGC

        print(num)

但这个问题有一个需要关注，即python的rounding issue。factorial得到的结果是float浮点数，相乘和相除的数过多会有误差。
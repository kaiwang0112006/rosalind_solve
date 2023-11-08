## Introduction to Alternative Splicing

### 问题

给定：两个正整数m和n (0≤m≤n≤2000)

输出：所有长度是k的子集合数 (m≤k≤n), 结果对1000000取余。

###  解决

和[Counting Subsets](https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/CountingSubsets/CountingSubsets.md)
的思路一样，只是循环从m开始，而不是1。

    def solution():
        n = 1846
        m = 688
        num = 0
        for i in range(m,n+1):
            comb = math.comb(n, i)
            num += comb
        print(num%1000000)

### 扩展

在蛋白质翻译的过程中，外显子被从前体RNA(pre-RNA)切出，重新组合为信使RNA(Messenger RNA, mRNA)。

但是外显子并不一定按照前体中的顺序组合。这个过程称为选择性剪接(Alternative splicing)，即基因中的所有外显子，并不一定全部按顺序组合为mRNA。
最常见的选择性剪切就是外显子跳跃(exon skipping)，指一个或多个外显子连同其两端的内含子一起被剪接，导致功能域/位点的丢失或
开放阅读框(Open Reading Frame, ORF)的框移。

选择性剪接在进化中有着至关重要的作用，它使得同一个基因可以翻译出大量不同的蛋白质。同一个基因因选择性剪切翻译产生的不同蛋白质称为蛋白质亚型(Protein Isoforms)。
实际上，95%的人类基因会被剪切为多种mRNA。选择性剪切出错会产生负面的突变。这被认为是遗传性疾病的一个发病原因。

在这个问题中，我们假设一个简单模型：一系列外显子可以连接为最终的mRNA。在这个假设下，设m是最小外显子数。转化为排列组合的数学问题后，就可以求出所有可能的
选择性剪切结果。
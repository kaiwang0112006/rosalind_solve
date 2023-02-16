## [Partial Permutations](https://rosalind.info/problems/pper/)

### 背景知识

**局部组合**: 从给定个数(n)的元素集合中取出指定个数(k)的元素进行排序(k<=n)。记为P(n,k)。

### 问题

给定：正整数n和k (100>=n>0, 10>=k>0)

输出：局部组合数据P(n,k)除以1000000取模

示例输入: 

    21 7

示例出: 

    51200

###  解决

    n = 21
    k = 7
    scipy.special.perm(n,k)%1000000
## [Edit Distance](https://rosalind.info/problems/edit/)

### 背景知识

**编辑距离(Edit Distance)**: 指从一个字符串转换到另一个字符串所需得最少操作次数。一般操作指的是替换，插入，删除单个字符。

### 问题

给定：以fasta格式提供的2个蛋白质序列

输出：计算编辑距离

### 解决

利用动态规划解决

    def edit_distance(str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
        return dp[m][n]

    print(edit_distance(str1, str2))

### 扩展

在[Counting Point Mutations](https://rosalind.info/problems/hamm/)， 我们认识到通过汉明距离可以给出进化距离概念，两个DNA序列的进化距离
就是计算两条序列的最小单点突变数目，也暗示了在进化路径上可能发生的变化数目。

但是实际上，同源的DNA序列很少是相同长度，因为点突变包含单碱基的插入和缺失。我们需要在之前的计算中考虑插入和缺失的情况。编辑距离就是最简单的实现。
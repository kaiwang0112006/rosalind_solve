## [Finding a Shared Spliced Motif](https://rosalind.info/problems/lcsq/)

### 背景

**最长公共子串(Longest Common Substring)与最长公共子序列(Longest Common Subsequence)**

公共子串是两个字符串中相同的一段子字符串，公共子序列与公共子串的区别是最长公共子序列不需要字符串完全相邻，
或者说不需要几个字符是连续出现的。如"ACTG"是"AACCTTGG"和"ACACTGTGA"的公共子序列。所有公共子序列中长度最长的就是
最长公共子序列。

### 问题

给定：一个fasta文件，包含2个DNA序列，长度约1kbp。

输出：一个最长公共子序列。(可能有多个，随机返回任意一个)

示例输入: 

    >Rosalind_23
    AACCTTGG
    >Rosalind_64
    ACACTGTGA

示例出: 

    AACTGG

###  解决

可以通过动态规划来解决，构建查询表

<a href="https://media.geeksforgeeks.org/wp-content/uploads/20230228150050/lcs7drawio.png" target="_blank"><img src="https://media.geeksforgeeks.org/wp-content/uploads/20230228150050/lcs7drawio.png" /></a>

    def lcs_fun(X, Y):
        m = len(X)
        n = len(Y)
        L = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
        # Following steps build L[m+1][n+1] in bottom up fashion. Note
        # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
            # Create a string variable to store the lcs string
        lcs = ""
    
        # Start from the right-most-bottom-most corner and
        # one by one store characters in lcs[]
        i = m
        j = n
        while i > 0 and j > 0:
    
            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if X[i - 1] == Y[j - 1]:
                lcs += X[i - 1]
                i -= 1
                j -= 1
    
            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
    
            else:
                j -= 1
    
        # We traversed the table in reverse order
        # LCS is the reverse of what we got
        lcs = lcs[::-1]
        print("LCS of " + X + " and " + Y + " is " + lcs)
        return lcs

### 扩展

在之前[Finding a Shared Motif](https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/FindingSharedMotif/FindingSharedMotif.md)中，
通过最长公共字串算法找到了两段序列字符串的公共字串，定义为“motif”。但当我们了解了RNA剪接之后，我们知道在DNA序列中有不表达的内含子。因此我们需要找到
分布在被分开的外显子中的motif，需要引入公共子序列(Common Subsequence)的概念。

## [Interleaving Two Motifs](https://rosalind.info/problems/scsp/)

### 背景知识

**公共超序**：如果字符串s包含字符串t，则s是t的超序。如果一个字符串即是s的超序，又是t的超序，则成为s和t的公共超序。如"ACGTACT"是"ACGTC"和"ATAT"
的公共超序。

### 问题

给定：给定两个DNA字符串s和t

输出：求s和t的最短公共超序。

示例输入: 

    ATCTGAT
    TGCATA

示例出: 

    ATGCATGAT

### 解决

这是一个动态规划问题，和“最长公共子序列”一样，现构造联结矩阵，再解析成字符串。

<a href="https://media.geeksforgeeks.org/wp-content/uploads/Shortest-Supersequence.jpg" target="_blank"><img src="https://media.geeksforgeeks.org/wp-content/uploads/Shortest-Supersequence.jpg" /></a>

    def printShortestSuperSeq(m, n, x, y):
        # dp[i][j] contains length of shortest
        # supersequence for X[0..i-1] and Y[0..j-1]
        dp = [[0 for i in range(n + 1)]
              for j in range(m + 1)]
    
        # Fill table in bottom up manner
        for i in range(m + 1):
            for j in range(n + 1):
    
                # Below steps follow recurrence relation
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif x[i - 1] == y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1])
    
        # string to store the shortest supersequence
        string = ""
    
        # Start from the bottom right corner and
        # add the characters to the output string
        i = m
        j = n
        while i * j > 0:

            if x[i - 1] == y[j - 1]:
    
                # Put current character in result
                string = x[i - 1] + string
    
                # reduce values of i, j and index
                i -= 1
                j -= 1
    
            # If current character in X and Y are different
            elif dp[i - 1][j] > dp[i][j - 1]:
    
                # Put current character of Y in result
                string = y[j - 1] + string
    
                # reduce values of j and index
                j -= 1
            else:
    
                # Put current character of X in result
                string = x[i - 1] + string
    
                # reduce values of i and index
                i -= 1
    
        # If Y reaches its end, put remaining characters
        # of X in the result string
        while i > 0:
            string = x[i - 1] + string
            i -= 1
    
        # If X reaches its end, put remaining characters
        # of Y in the result string
        while j > 0:
            string = y[j - 1] + string
            j -= 1
    
        return string

### 扩展

在[Finding a Shared Spliced Motif](https://rosalind.info/problems/lcsq/)中，我们借助公共子序列(Common Subsequence)的概念找到
两个序列的公共motif，且可以分布在不同的exon上。本问题，我们反过来思考，在得到两个不同的motif后，产生能够同时包含两个motif的最短序列。
# -*- coding: utf-8 -*-

# A dynamic programming based Python3 program print
# shortest supersequence of two strings

# returns shortest supersequence of X and Y


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

    # Following code is used to print
    # shortest supersequence

    # dp[m][n] stores the length of the
    # shortest supersequence of X and Y

    # string to store the shortest supersequence
    string = ""

    # Start from the bottom right corner and
    # add the characters to the output string
    i = m
    j = n
    while i * j > 0:

        # If current character in X and Y are same,
        # then current character is part of
        # shortest supersequence
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


# Driver Code
if __name__ == "__main__":
    x = "TCTAAATTAAGAGTTGCACCTTGGCAGAGCCGCTTCTAGTCTGAAATTATAGTGGGTACCATTGAACATCGCCCGCATCCCCCCA"
    y = "CTACACCATTGCATCGAGTTTGCAGCATGTTGGCGGGACAGGACCGTTGCGTGGCAGTCCCAACTACGTCGTCTATGCACCCTACAG"
    m = len(x)
    n = len(y)

    # Take the smaller string as x and larger one as y
    if m > n:
        x, y = y, x
        m, n = n, m

    print(printShortestSuperSeq(m, n, x, y))

# This code is contributed by
# sanjeev2552
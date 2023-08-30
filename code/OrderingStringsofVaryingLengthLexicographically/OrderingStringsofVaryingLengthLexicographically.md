## [Ordering Strings of Varying Length Lexicographically](https://rosalind.info/problems/lexv/)

### 问题

给定：一个字符串和一个数字n (n<=4)

输出：从字符串中选取k个的全排列(1<=k<=n)，按字典序排序，字典序由给定字符串确定

###  解决

可以用**itertools**对字符串的每个长度做笛卡尔积。

    def solve():
        n = 3
        alphabet = 'Q O E W'.replace(" ","")
        perm = []
        for i in range(1, n + 1):
            perm.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))
        permutations = list(itertools.chain(*perm))
        srt_perm = sorted(permutations,key=lambda word: [alphabet.index(c) for c in word])
        with open("r.txt",'w') as f:
            r = '\n'.join(srt_perm)
            f.write(r)


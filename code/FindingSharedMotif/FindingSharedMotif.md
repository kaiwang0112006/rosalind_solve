## Finding a Shared Motif

### 背景知识

**公共子串**: 两个字符串包含的相同的子字符串。

### 问题

给定：一个fasta文件，包含k个DNA序列(k<=100)，每个序列长度不大于1kbp

输出：所有序列的最大公共子串

###  解决

核心问题是如何高效拿到两个字符串的公共子串，之后只需要循环就可以了。

寻找两个字符串的公共子串的方法参考[LONGEST COMMON SUBSTRING ALGORITHM](https://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php)的方法。

    def lcs(S,T):
        #print(S,T)
        #print(type(S), type(T))
        m = len(S)
        n = len(T)
        counter = [[0]*(n+1) for x in range(m+1)]
        longest = 0
        lcs_set = set()
        for i in range(m):
            for j in range(n):
                if S[i] == T[j]:
                    c = counter[i][j] + 1
                    counter[i+1][j+1] = c
                    if c > longest:
                        lcs_set = set()
                        longest = c
                        lcs_set.add(S[i-c+1:i+1])
                    elif c == longest:
                        lcs_set.add(S[i-c+1:i+1])
        #print(lcs_set)
        return lcs_set, longest
    
    def main():
        record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
        idlist = list(record_dict.keys())
        com, l = lcs(str(record_dict[idlist[0]].seq),str(record_dict[idlist[1]].seq))
    
        for i in range(2, len(idlist)):
            comdict = {}
            for sq in com:
                com_sub, l = lcs(sq,str(record_dict[idlist[i]].seq))
                comdict[l] = com_sub
            com = comdict[max(comdict.keys())]
    
        print(com)
## Speeding Up Motif Finding

### 背景知识

1. 字符串的前缀和后缀: 字符串从第一个字符开始向后延申的子字符串即前缀，从最后一个字符串向前延申的子字符串是后缀。

2. 匹配数组(failure array): BMP算法(Knuth-Morris-Pratt algorithm)的中间查询矩阵，用于查找下一次位移的位置。长度为n的字符串s对应一个长度
为n的数组，第k个位置的值为与前缀s[1:k−j+1]相同的最长后缀子字符串s[j:k]，其中j不等于1。

### 问题

给定：一个fasta文件，其中第一个序列为100kbp左右的DNA序列

输出：匹配数组

###  解决

这个问题最大的难点是效率，通过正则匹配可以提高字符串匹配的效率。

    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        dna = str(record_dict[k].seq)
    flag = True
    farr = np.zeros(len(dna), dtype=np.int32)

    i = 1
    while flag:
        print(i)
        mat = re.finditer("(?=(%s))" % dna[:i], dna[1:])

        flag = False
        for m in mat:
            idx = m.end(1)
            farr[idx] = len(dna[:i])
            #print(dna[:i],dna[idx-i+1:idx+1])
            flag = True

        i += 1
    
    print(" ".join([str(i) for i in farr]))

### 扩展

BMP算法(Knuth-Morris-Pratt algorithm)
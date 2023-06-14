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

*BMP算法(Knuth-Morris-Pratt algorithm)*:

Knuth-Morris-Pratt算法简称KMP算法，它的名字是由著名的三位科学家名字组合而成。KMP算法是一种高效的字符串查找算法，它性能高效的原因在于它会利用字符串匹配过程中失败的信息，从而减少字符串查找比较的次数。

KMP算法借助了一个辅助的结构部分匹配表(failure array)，部分匹配表是对搜索词分析产生的一个信息表，部分匹配值是某个字或字母对应的“前缀”和“后缀”的最长共有元素的长度。

假设要匹配的字符串为abababca, 对于第一个a，它的前缀和后缀均为空集，因此共有元素的长度为0。对于ab，前缀为a, 后缀为b，两者的共有元素长度为0。
对于aba, 前缀为(a,ab)，后缀为(a,ba),因此两者的共有元素长度为len(a)=1。对于abab, 有三个前缀(“a”，“ab”和“aba”)和三个后缀(“bab”，“ab”和“b”),
两者的共有元素长度为len(ab)=2。依次类推，结构部分匹配表为:

    char:  | a | b | a | b | a | b | c | a | 
    index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 
    value: | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |

假设我们的目标字符串为"bacbababaabcbab",要匹配"abababc", 我们首先匹配到的是:

    bacbababaabcbab
     |
     abababc

当移动到上图时,匹配到了"a"，且后面没有匹配，需要后移继续匹配，但是如果只后移一位，计算复杂度较高，因此KMP算法提供一种方法可以后移多位，减少比对次数。
移动位置计算方式为: 移动位数 = 当前已经匹配的字数 - 最后一个匹配字的匹配值, 上面匹配的"a"的匹配值可以查结构部分匹配表，为0，当前已经匹配的字数为1，因此
后移一位。

    bacbababaabcbab
        |||||
        abababca

上面这个匹配情况，最后一个匹配字的匹配值查表得3，当前已经匹配的字数为5，移动位数为5-3=2。

经过上述KMP算法的匹配过程，可以发现对于被匹配的字符串不再存在重复匹配的问题，被搜索字符串都会被依次往下进行匹配，匹配性能会高于传统字符串一一对照比较方式。
不同点在于需要将搜索词建立部分匹配表，建立部分匹配表的时间复杂度为O(n)。




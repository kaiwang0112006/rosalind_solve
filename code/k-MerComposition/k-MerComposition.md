## [k-Mer Composition](https://rosalind.info/problems/kmer/)

### 问题

给定：一个DNA序列s（长度约100bp，FASTA）

输出：s中4-mer出现频率

### 解决

首先以长度为4的窗口滑动整个序列，得到4-mer出现频率的字典。

    cdict = {}
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        a = str(record_dict[k].seq)
    for i in range(len(a)-4+1):
        kmer = a[i:i+4]
        if kmer not in cdict:
            cdict[kmer] = 1
        else:
            cdict[kmer] += 1

然后以ATCG产生4-mer，并排序，根据上一步得到的字典匹配频率打印。

    b = Counter(a)
    c = list(b.keys())

    klist = []
    for i in itertools.product(c, repeat = 4):
        klist.append(''.join(i))
    klist = sorted(klist)
    rlist = []
    for i in klist:
        if i in cdict:
            rlist.append(str(cdict[i]))
        else:
            rlist.append('0')
    print(" ".join(rlist))

### 扩展

长度为k的子字符串被称为k-mer。一个序列可以由n-k+1个k-mer覆盖。对于一个字符串，k-mer的出现频率被称为k-mer构成(k-mer composition)。 如：
{"ACTT":45,"AACC":34...}

1-mer就是DNA序列的GC含量。而2-mer, 3-mer, 4-mer被称为di-nucleotide, tri-nucleotide, tetra-nucleotide compositions。

k-mer的生物学重要性有很多。GC含量可以用于识别未知的DNA序列，高GC含量的区域可能是外显子。k-mer分析是序列组装的关键步骤。

通过子字符串分析而不是单个字符分析，长的k-mer可以提供字符串的有效表证。在语言分析中，k-mer可以用于确认语言和作者。
## [Error Correction in Reads](https://rosalind.info/problems/corr/)

### 问题

给定：一个fasta文件，包含1000个序列，长度约50bp，有一些序列包含单碱基错误。所有序列的数据集包含两种情况
    
1). 正确的序列: 在数据集中出现至少两次(可能包含反向互补)

2). 不正确的序列: 在数据集中只出现一次，与数据集中的正确序列(或反向互补序列)的汉明距离为1，即只差一个碱基。

输出：所有序列突变关系，表示为"[旧序列]->[新序列]"。

示例输入: 

    >Rosalind_52
    TCATC
    >Rosalind_44
    TTCAT
    >Rosalind_68
    TCATC
    >Rosalind_28
    TGAAA
    >Rosalind_95
    GAGGA
    >Rosalind_66
    TTTCA
    >Rosalind_33
    ATCAA
    >Rosalind_21
    TTGAT
    >Rosalind_18
    TTTCC

示例出: 

    TTCAT->TTGAT
    GAGGA->GATGA
    TTTCC->TTTCA

###  解决

整体需要两次循环(除了文件解析外)。

(1). 汉明距离

首先解决汉明距离的计算

    def hammingDist(str1, str2):
        i = 0
        count = 0
        while (i < len(str1)):
            if (str1[i] != str2[i]):
                count += 1
            i += 1
        return count

(2). fasta文件读取

文件解析需要得到两个中间结果，一个字典存储序列和反向互补序列，减少后续重复计算。还有一个记录序列出现次数(包含反向互补序列)，用于区分正确和错误的序列。

    sequences_count = {}
    seqmap = {}
    seqmap_r = {}
    # fasta parser
    handle = open('sampledata.fasta', 'r')
    for record in SeqIO.parse(handle, 'fasta'):
        orgseq = str(record.seq)
        reverseseq = str(record.reverse_complement().seq)
        seqmap[orgseq] = reverseseq
        seqmap[reverseseq] = orgseq

        if reverseseq in sequences_count:
            sequences_count[reverseseq] += 1
        elif orgseq in sequences_count:
            sequences_count[orgseq] += 1
        else:
            sequences_count[orgseq] = 1

(3). 区分正确和错误的序列

第一次循环区分正确和错误的序列，正确的序列出现次数不等于1，错误的序列只出现一次。

    # separate correct and incorrect
    correct_seqs = []
    incorrect_seqs = []
    for s in sequences_count:
        if sequences_count[s] == 1:
            incorrect_seqs.append(s)
        else:
            correct_seqs.append(s)

(4). 提取突变序列对

第二次循环是一个两重循环，外层循环错误序列，内层循环正确序列，并获取反向互补序列，分别计算汉明距离并判断。

    # cal error reads
    for i in range(len(incorrect_seqs)):
        for j in range(len(correct_seqs)):
            seq1 = incorrect_seqs[i]
            seq2 = correct_seqs[j]
            seq3 = seqmap[seq2]
            if hammingDist(seq1, seq2) == 1:
                seqorder = sorted([seq1, seq2])
                seqmap_r[tuple(seqorder)] = [seq1, seq2]
            elif hammingDist(seq1, seq3) == 1:
                seqorder = sorted([seq1, seq3])
                seqmap_r[tuple(seqorder)] = [seq1, seq3]

    for tu in seqmap_r:
        print("%s->%s" % (seqmap_r[tu][0],seqmap_r[tu][1]))

### 扩展

基因组测序并不完美，测序仪会存在大量的测序错误且无法预测，因此在基因组组装之前，纠正测序错误是一个关键步骤。


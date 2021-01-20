## Open Reading Frames

### 背景知识

**开放阅读框**: 开放阅读框(Open Reading Frame, ORF)从起始密码子开始，是DNA序列中具有编码蛋白质潜能的序列，结束于终止密码子连续的碱基序列。在[Transcribing DNA into RNA](http://rosalind.info/problems/rna/)和[Translating RNA into Protein](http://rosalind.info/problems/prot/)中已经知道，DNA翻译成蛋白质一级结构是通过每三个连续碱基(即三联“密码子”）编码相应的氨基酸。因此，每条DNA有三种可能的阅读框，即从第一个碱基开始，第二个碱基开始，第三个碱基开始三种可能，双链DNA就有六种ORF，当然还需要考虑从其实密码子开始，到终止密码子结束。

### 问题

给定：一个fasta文件，包含1个DNA序列，长度不大于1kbp

输出：根据DNA的ORF可以翻译成的所有氨基酸序列。

###  解决

根据给定序列，如“AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG”，先经过两重循环，外层循环以字符串的第1，2，3个字符开始切割字符串，内层循环考虑DNA的互补链。切割后先翻译成氨基酸序列，然后通过正则匹配，找到所有起始密码子到终止密码子之间的序列。当然还要记得去重。

    rlist = []
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        for st in range(3):
            s = record_dict[k].seq[st:].translate()
            #print(s)
            for aa in re.findall(r"(?=(M[A-Z]*\*))",str(s)):
                rlist.append(aa[:-1])
            s = record_dict[k].reverse_complement().seq[st:].translate()
            #print(s)
            for aa in re.findall(r"(?=(M[A-Z]*\*))",str(s)):
                rlist.append(aa[:-1])
    for s in set(rlist):
        print(s)

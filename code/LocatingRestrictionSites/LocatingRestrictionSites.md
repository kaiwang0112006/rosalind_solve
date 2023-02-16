## Locating Restriction Sites

### 背景知识

**反向回文(reverse palindrome)**: 一个DNA序列的互补链和该序列相同

### 问题

给定：一个fasta文件，包含1个DNA序列，长度不大于1kbp

输出：所有符合反向回文的DNA子序列的起始位置和长度

###  解决

只需要构建判断是否为反向回文的函数，循环序列切割子序列即可。

    def isPalindrome(s):
        s = s.upper()
        sv = s[::-1]
        smap = {"A":"T","T":"A","C":"G","G":"C"}
        #print(sv)
        #sv = sv.translate(str.maketrans('ACGT', 'TGCA'))
        sv = ''.join([smap[i] for i in sv])
        #print(sv,s)
        return sv == s

    def main_fast():
        record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
        for k in record_dict:
            seq = record_dict[k].seq
        for i in range(len(seq)-3):
            lmax = min(len(seq[i:]),12)
            if lmax % 2 !=0:
                 lmax = lmax+1
            for ll in range(4,lmax+1,2):
                subseq = seq[i:i+ll]
                if isPalindrome(subseq):
                    print(i+1,ll)

### 扩展

噬菌体是一类通过感染和寄生于细菌来繁殖的病毒。它会将自己的DNA插入到细菌的DNA中，利用细菌的细胞功能来转录翻译繁殖噬菌体个体。限制性内切酶就是细菌抵御噬菌体侵染的一种机制。

限制性内切酶是一类同二聚体。可以识别DNA双链上固定的4-12长度的核苷酸序列，即噬菌体DNA中的回文结构，通过结合并切割这段特定的DNA序列使噬菌体DNA被切割失效。

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

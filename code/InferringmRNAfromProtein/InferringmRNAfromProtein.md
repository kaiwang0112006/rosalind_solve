## Inferring mRNA from Protein

### 背景知识

取模运算：数学上，假设a是一个正整数，如果a/n的余数是b，则称b是n除以a的模，记作 a≡b mod n

### 问题

给定：一个长度不超过1000的蛋白质序列

输出：可以翻译得到这个蛋白质序列的mRNA序列数，即可反转录成多少种mRNA序列，结果取除以1,000,000的模

### 解决

只是一个排列组合问题，首先找出反转录序列表，得到每个位置可以反转录得到的mRNA序列种类数，相乘即可

    def main():
        proteincoden = {'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'C': ['UGU', 'UGC'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'],
         'F': ['UUU', 'UUC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'H': ['CAU', 'CAC'], 'I': ['AUA', 'AUU', 'AUC'],
         'K': ['AAA', 'AAG'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'M': ['AUG'], 'N': ['AAU', 'AAC'],
         'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
         'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
         'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'W': ['UGG'], 'Y': ['UAU', 'UAC'], '_': ['UAA', 'UAG', 'UGA']}
    
        protein = "MIKPIIIAPLWWAYGDDIMSDIMYRKTNHSWIIMGMKAAGVCADHTCVCDAFVGQHHGFMVCCEFTLSASWAHKEMCRTMMTTASWAHPVPARAMSNWVAKPFWCTAKVARTLDLAVQPNKMKCDSEPCDRIVVNMCDAASIIGLFSCMEELIDDDMDIYERINASNFSFADQLYCTAPVRTWAPPFWYRTDSKFAKKCCQNCKKWWEAVWSDWDGDMYWRMSRTENTTWGGKEGDYCACTQFHENSNIPCPRMTDCISQSLWLHLAYCVKLKDMFYNGMMNMATSMCTQKSGQCFKIWCMIVAQLLFFRRAHCQLLVIMVLGQYKCECHCTVKFGGPSVGAQKRITPFNTEQKGWPNTRAPIKSEPYRSTFIPNHCAPYRAMKMDQYIFNEFWVTGRMYAFRVEPNCGPRCISIRDCYLNIHLNVEFTEFIWHDQRIGRGIMSRIYLGVFNTKTHYFNYLEVHSNTHDDCGVMFWDGIPVTAEADNDCGMCLGVYAMVKMNCNTCMYPFFDLMDPPWEGCTLFHKYEQVCCMCRYPRFPRTLNQALFLDNALPRCDNVKEGSGIQPCCEEDHLTLWRPLHWLKWNYVNMKKYRPFEYSSILPNPGGVWTQNYWVFCHKPEAFVFKCYYLMTDLDLTTPIGHVLWSRRRHTCIARAQSKDHHQTIELNAMKNSFWTMMPVKFHQDCITLPGVMWFDWWGNMVESAHAHIRVWLKKCAKCAPFMKTTIEGENAPCTVFRMLWHCWANFPWEMFPYYEYGPMGYGMCYDEWETFRYYDERTPTEHSTWITYSYSDECWSHDCIPIIPVTKYRFFSNFAIGRFQEGTTCRRCMVGFGTYQAAIDAWGSCLVGHPIRIPVFCEHFAYAWGGYWWWEFPDYRRMCRELAHHTAWHNQLCNDKRMWWVCMCLFYMYMNWEAWRLHMGKETFFSRHFNAWWVPERGPALTFRCTSPTGVHKNIAHSQVTCQRKFDMFHHKIKVEHGFIDCDMCVMQSWMRQGIIAIL"
        n = 1
        for aa in protein:
            n = n*len(proteincoden[aa])
        n = n*len(proteincoden['_'])
        print(n%1000000)
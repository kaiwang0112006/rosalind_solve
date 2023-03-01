## [Transitions and Transversions](https://rosalind.info/problems/tran/)

### 背景知识

**转换和颠换比例(transition/transversion ratio)**

点突变，也称作单碱基替换，指由单个碱基改变发生的突变，可以分为转换(transitions)和颠换(transversions)两类。转换指嘌呤和嘌呤之间的替换，或
嘧啶和嘧啶之间的替换。颠换指嘌呤和嘧啶之间的替换。

<a href="https://rosalind.info/media/transitions-transversions.png" target="_blank"><img src="https://rosalind.info/media/transitions-transversions.png" /></a>

### 问题

给定：两个长度相同的DNA序列s1和s2

输出：两个序列的转换和颠换比例

示例输入: 

    >Rosalind_0209
    GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
    AGTACGGGCATCAACCCAGTT
    >Rosalind_2200
    TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
    GGTACGAGTGTTCCTTTGGGT

示例出: 

    1.21428571429

###  解决

    s1 = 
    s2 = 

    transitionsmap = [("A","G"),("G","A"),("C","T"),("T","C")]
    transversionsmap = [("A","C"),("C","A"),("T","G"),("G","T")
        ,("A","T"),("T","A"),("C","G"),("G","C")]

    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        pos = (s1[i],s2[i])
        if pos in transitionsmap:
            transitions += 1
        elif pos in transversionsmap:
            transversions += 1
        else:
            pass

    print(transitions/transversions)

### 扩展

点突变，也称作单碱基替换，指由单个碱基改变发生的突变，可以分为转换(transitions)和颠换(transversions)两类。转换指嘌呤和嘌呤之间的替换，或
嘧啶和嘧啶之间的替换。颠换指嘌呤和嘧啶之间的替换。

由于转换没有改变碱基的结构，而颠换使碱基的化学结构发生较大变化，因此转换比颠换更加常见。在整个基因组上，一般转换和颠换比例平均为2，但是在编码区，比例会
高一些，经常超过3。有的转换不会改变编码的氨基酸，也不会改变蛋白质结构，因此被称为沉默替换。

转换和颠换比例是一个快速有效的基因组分析统计指标，因为可以快速定位编码DNA。
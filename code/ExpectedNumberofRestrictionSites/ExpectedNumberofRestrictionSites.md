## [Expected Number of Restriction Sites](https://rosalind.info/problems/eval/)

### 问题

给定：一个正整数n(n<=1000000)，一个DNA序列s，长度为偶数，不大于10，以及一个数组A，长度大约为20，包含一系列0到1之间的小数。

输出：一个数组B，长度和A一样，B[i]代表序列s是一个长度为n的随机序列t的子字符串的预期出现次数。t是由A[i]代表的GC含量构造的。

###  解决

核心计算逻辑就是概率的乘积

    def expected_number(self, length, motif, gcc):
        map = {}
        map['G'] = map['C'] = gcc / 2
        map['A'] = map['T'] = (1 - gcc) / 2
        number_of_positions = length - len(motif) + 1
        chance = 1
        for c in motif:
            chance *= map[c]
        return round(number_of_positions * chance, 3)

### 扩展

在[Locating Restriction Sites](https://rosalind.info/problems/revp/)我们认识了限制性内切酶(restriction enzymes)。细菌中这些酶
能双向剪切病毒DNA，使病毒失活。病毒DNA上的这些酶切位点称为限制性酶切位点(restriction sites)。限制性内切酶能够识别DNA序列上特定的反向回文片段
，并结合切割，称为识别序列/酶切序列(recognition sequence)。这些序列通常为偶数长度，一般4-6的碱基，也有更长的。

在这个问题中，我们首先有一个疑问：细菌是怎么知道它能够在病毒DNA上找到限制性酶切位点？我们认为，识别序列的长度较短，保证了能够随机产生大量的匹配。

进一步，我们把问题具象化，将GC含量考虑进去。

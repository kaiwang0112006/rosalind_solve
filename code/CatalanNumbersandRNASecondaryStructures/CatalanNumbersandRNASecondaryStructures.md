## [Catalan Numbers and RNA Secondary Structures](https://rosalind.info/problems/cat/)

### 背景知识

**1. 完美匹配 (Perfect matching)**

在一张图G上，当所有两点以边相连，且没有点属于多个边的时候, 整体成为一个“匹配”。如果G有偶数个点(2n)，如果一个“匹配”包含n个边，即最大可能数，
因为包括了图中的所有点， 这一匹配称为“完美匹配”。

**2. 非相交匹配 (Noncrossing match)**

如果一个图中匹配的边没有相交，就称为非相交边(noncrossing)。如果把图上的n个点按从1到n的序号编号，那么只要一个匹配的任意两个边{i,j}和{k,l}没有
i<k<j<l，是非相交匹配。

**3. 卡特兰数 (Catalan numbers)**

计算一个完全图的非相交匹配，可以通过卡特兰数来表示。用Cn表示一个完全图K2n中的非相交匹配个数。图中的点用1到2n的数字编号。我们可以把1和其他任何
剩余的2n-1个点连接成边。如我们连接1和m，那么为了剩下的边不与{1,m}这条边相交，我们只能把两侧的点各自相连。因此，m一定是偶数，可以写做m=2k。这时候，
有2k-2个点在{1,m}的一侧，2n-2k个点在{1,m}的另一侧。最终结果可以写成递推关系式：

<img src="https://latex.codecogs.com/svg.image?\inline&space;\bg{white}&space;&space;&space;C_{n}=\sum_{k=1}^{n}c_{k-1}c_{n-k}" title="https://latex.codecogs.com/svg.image?\inline \bg{white} C_{n}=\sum_{k=1}^{n}c_{k-1}c_{n-k}" />

这个递推关系式叫做卡特兰数(Catalan numbers): h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)h(0)

### 问题

给定：一个fasta文件，包含一条RNA序列s，长度约300bp，A和U的数目相同，C和G的数目相同。

输出：所有不相交完美匹配的数目，结果对1000000取模。

示例输入: 

    >Rosalind_57
    AUAU

示例出: 

    2

###  解决

可以用动态规划来求解。为了减少计算量，将已计算的结果放到字典中。

    def ispair(a, b):
        if a == "A" and b == "U":
            return True
        elif a == "U" and b == "A":
            return True
        elif a == "G" and b == "C":
            return True
        elif a == "C" and b == "G":
            return True
        else:
            return False
    
    
    def catalan(dna, cata):
        if dna in cata:
            return cata[dna]
        n = len(dna)
        c=0
        for m in range(1, n, 2):
            if ispair(dna[0], dna[m]):
                c += (catalan(dna[1:m], cata) * catalan(dna[m+1:], cata))
        cata[dna] = c
        return cata[dna]
    
    def main():
        sequence = ''
        handle = open('sampledata.fasta', 'r')
        for record in SeqIO.parse(handle, 'fasta'):
            sequence = str(record.seq)
        handle.close()
        cata = {'': 1, 'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1}
        print(catalan(sequence, cata) % 1000000)

### 扩展

在RNA折叠中，RNA的二级结构的预测应该避免碱基间的相互交叉，即假结(pseudoknot)。
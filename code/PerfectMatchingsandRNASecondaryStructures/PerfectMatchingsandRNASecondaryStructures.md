## [Perfect Matchings and RNA Secondary Structures](https://rosalind.info/problems/pmch/)

### 背景知识

**1. 完全图 (Complete graph)**

在图论的数学领域，完全图是一个简单的无向图，其中每对不同的顶点之间都恰连有一条边相连。完整有向图(complete digraph)是一个有向图，
其中每对不同的顶点通过一对唯一的边缘（每个方向一个）连接。

**2. 二分图 (Bipartite graph) 和完全二分图 (Complete bipartite graph)**

二分图是图论中一种特殊模型。指顶点可以分成两个不相交的集使得在同一个集内的顶点不相邻（没有共同边）的图。 完全二分图是一种特殊的二分图， 第一个子集的
顶点和第二个子集的顶点全部相连，有且只有一条边相连。

**3. 完美匹配 (Perfect matching)**

在一张图G上，当所有两点以边相连，且没有点属于多个边的时候, 整体成为一个“匹配”。如果G有偶数个点(2n)，如果一个“匹配”包含n个边，即最大可能数，
因为包括了图中的所有点， 这一匹配称为“完美匹配”。

记K2n是一个完全图，包含2n个点，每个点都和其他所有点通过边相连。pn记为K2n的所有完美匹配。对于图中的点x，有2n-1个边将x与图中其他点相连。如果要形成
一个完美匹配，还需要处理剩下的2n-2个点，这个递归逻辑最后得到公式:

<img src="https://latex.codecogs.com/svg.image?p_{n}&space;=&space;(2n-1)(2n-3)(2n-5)\cdots&space;(3)\;&space;\:&space;\:&space;\:&space;\:&space;\:&space;\;&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;\:&space;(1)" title="https://latex.codecogs.com/svg.image?p_{n} = (2n-1)(2n-3)(2n-5)\cdots (3)\; \: \: \: \: \: \; \: \: \: \: \: \: \: \: \: \: \: \: \: \: (1)" />     

**4. RNA的结合键图 (Bonding graph)**

对于一个RNA序列s=s1s2...sn，结合键图 (bonding graph)的构建包含下面几个步骤。首先，每个碱基按顺序排列成一个圆形，相邻碱基通过边相连，这类边叫做
相邻边(adjacency edges)，所有的{A,U}和{C,G}相连，这类边叫做碱基对边(basepair edges)

<img src="https://rosalind.info/media/problems/pmch/bonding_graph.png" title="bonding_graph"/>

在这张图上每一个碱基对边的完美匹配代表了一种可能的碱基对相互作用形式。而这种完美匹配存在的前提是A和U的数目相同，C和G的数目相同。

<img src="https://rosalind.info/media/problems/pmch/bonding_crossing.png" title="bonding_crossing"/>

### 问题

给定：一个fasta文件，包含一条RNA序列s，长度约80bp，A和U的数目相同，C和G的数目相同

输出：s的结合键图 (bonding graph)中碱基对边的完美匹配的数目

示例输入: 

    >>Rosalind_23
    AGCUAGUCAU

示例出: 

    12

###  解决

可以拆分成两个完全二分图: AU配对和CG配对。我们可以通过公式(1)计算每个完全二分图的完美匹配的数目。假设n1是A的数目，n2是C的数目，所需要的解为：

<img src="https://latex.codecogs.com/svg.image?matchings&space;=&space;n1!*n2!" title="https://latex.codecogs.com/svg.image?matchings = n1!*n2!" />

    from Bio import SeqIO
    from math import factorial
    
    def main():
        sequence = ''
        handle = open('sampledata.fasta', 'r')
        for record in SeqIO.parse(handle, 'fasta'):
            sequence = str(record.seq)
        handle.close()
    
        AU = 0
        GC = 0
        for nt in sequence:
            if nt == 'A':
                AU += 1
            elif nt == 'G':
                GC += 1
    
        matchings = factorial(AU) * factorial(GC)
        print(matchings)
    
    if __name__ == "__main__":
        main()

### 扩展

相似的物种会有很多相通的基因，但会有修改/变化。因此，在比较两个基因组时，可以通过分析基因排列推断哪些重组导致基因分开。

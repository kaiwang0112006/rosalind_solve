## [Distances in Trees](https://rosalind.info/problems/nwck/)

### 背景知识

**1. Newick格式**

Newick 是最常见的进化树文件格式，了解这种格式之前，有必要先掌握树状结构的构成。首先来看一个tree的示例：

<a href="" target="_blank"><img src="https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/DistancesinTrees/NDA.png?raw=true" /></a>

在上述示例中，一共有A-F共6个节点。其中A-D, 通常称之为叶子节点leaf nodes， 叶子节点往下在没有其他的节点了; E称之为内部节点internal nodes，
往下还有其他的节点；F称之为根节点root node,  是整个树中所有节点的公共祖先。

通过圆括号的嵌套区分不同层级，然后就可以表示出一个完整的树，上述的tree表示为：(A,B, (C,D)E)F

上述的表示方式缺少了分支的信息，对于分支的信息，将其当做节点的属性来表示，和节点的名称之间用冒号:分割，比如A:0.1。当加上分支信息后，
上面的tree表示为(A:0.1,B:0.2,(C:0.3, D:0.4)E:0.5)F


### 问题

给定：n棵Newick格式的树，每棵树最多200个节点。用分号分割下一行给出树的两个节点。

输出：计算每棵树上给出的两个节点的距离。

### 解决

Biopython中有Newick格式的解析工具，可以偷个懒，但是需要附上两两节点的长度。

    from Bio import Phylo
    import io
    
    #open file and parse data
    f = open('rosalind_nwck.txt','r')
    pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]
    a = ''
    for i, line in pairs: # '(cat)dog;' as Newick format tree, 'dog cat' as two nodes to cal distance
        x,y = line.split()
        tree = Phylo.read(io.StringIO(i),'newick')
        #Phylo.draw(tree)
        clades = tree.find_clades()
        for clade in clades:
            clade.branch_length = 1  #  assign the branches a length of 1
        a +=('%s' % tree.distance(x,y) + ' ')
    print(a)
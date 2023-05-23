## [Counting Phylogenetic Ancestors](https://rosalind.info/problems/inod/)

### 背景知识

#### 二叉树(Binary Tree)

二叉树在图论中是这样定义的: 二叉树是一个连通的无环图，并且每一个顶点的度不大于3。二叉树是构建系统发育树的重要工具。

有根树(Rooted Tree)是指树中一个节点被指定为根(root)。图论中，一般定义树中任意两个节点只有一条路径。

无根二叉树可以包含两度的节点，所有内节点是三度。有根数根结点的度为2，其他内结点的度为3。


### 问题

给定：一个正整数n(3≤n≤10000)

输出：一个拥有n个叶子节点的无根二叉树的内节点数

### 解决

这个问题不需要编程。如图所示

<a href="" target="_blank"><img src="https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/CountingPhylogeneticAncestors/pic1.png?raw=true" /></a>
<a href="" target="_blank"><img src="https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/CountingPhylogeneticAncestors/pic2.png?raw=true" /></a>

设内节点数是k，叶子节点数是n，遍历所有的边两遍，得到3k+n = 2((k+n)-1), 所以k=n-2。

### 扩展

在[之前](https://github.com/kaiwang0112006/rosalind_solve/blob/main/code/CompletingaTree/CompletingaTree.md)我们定义了
用树来描述系统发育，但是哪种图更适合做系统发育研究呢？

根据现代进化理论(从达尔文进化开始)，新物种的产生，通常是因为与一个已有物种发生一段时间的隔离。在这一理论下，系统发育的可以用二叉树来表示，
内节点代表一个祖先物种，可以进化为一个或者两个新物种。

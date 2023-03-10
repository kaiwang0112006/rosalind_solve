## [Completing a Tree](https://rosalind.info/problems/tree/)

### 背景知识

#### 树(Tree)

在这里树定义为没有环(cycles)的无向图。

### 问题

给定：一个正整数n代表节点数以及一个邻接矩阵代表图中边

输出：这张图能够变成树所需的最小新增边数目

### 解决

首先找到图中有多少子图，以及孤立点数，新增边数目即为子图数-1+孤立点数

    def main():
        G = nx.Graph()
        with open(r'rosalind.txt', "r") as f:
            n_nodes = int(f.readline())
            adjacency_list = [line.strip().split() for line in f]
            nodes = set()
            for i, j in adjacency_list:
                G.add_node(i)
                G.add_node(j)
                G.add_edge(i,j)
                if not i in nodes:
                    nodes.add(i)
                if not j in nodes:
                    nodes.add(j)
    
        ntrees = len(list(nx.connected_components(G)))
        print(ntrees-1+n_nodes-len(nodes))

### 扩展

虽然达尔文的进化论已经发表了一个多世纪，一棵完整的进化的树还没有构建出来。可能90%的物种还没有被编目。如果感兴趣的话,可以去看
[Tree of Life Web Project](http://www.tolweb.org/tree/)。该项目始于1995年，目前所包含的不同物种和进化历史已经
多达10000多页。

虽然还不能构建完整的生命树，我们可以构建一个简单的树，其中一些物种已经进行了合并，合并后的分组称为类群(taxon)。系统发育树就是这样
的树型图，用于表证不同类群的进化关系，而进化树的构建依赖于我们对进化关系的特定假设。

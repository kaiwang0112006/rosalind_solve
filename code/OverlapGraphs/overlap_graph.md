## Overlap Graphs

### 背景知识

1. 有向图(directed graph)
2. 邻接表(adjacency list)
3. 交叠图(overlap graph, 自己翻译的)

### 问题

给定：一个fasta文件，包含若干序列，总长10kbp。

输出：邻接表(adjacency list)，overlap长度定义为3

<br>
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

###  解决

直接两层循环序列列表，头尾有overlap则打印一行邻接表

    def main():
        k = 3
        record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
        idlist = list(record_dict.keys())
        ajlist = []
        for s in range(len(idlist)):
            for t in range(s+1, len(idlist)):
                ssq = record_dict[idlist[s]].seq
                tsq = record_dict[idlist[t]].seq
                if ssq[:k] == tsq[(-1)*k:]:
                    print(idlist[t], idlist[s])
                elif tsq[:k] == ssq[(-1)*k:]:
                    print(idlist[s], idlist[t])
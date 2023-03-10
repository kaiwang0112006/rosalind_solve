# -*- coding:utf-8 -*-

import networkx as nx

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





if __name__ == "__main__":
    main()
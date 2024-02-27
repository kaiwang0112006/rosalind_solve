# -*- coding:utf-8 -*-

import sys
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
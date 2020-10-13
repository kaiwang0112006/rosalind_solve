# -*- coding:utf-8 -*-
from Bio import SeqIO
import collections
import copy

'''
problem: http://rosalind.info/problems/grph/
'''

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

if __name__ == "__main__":
    main()
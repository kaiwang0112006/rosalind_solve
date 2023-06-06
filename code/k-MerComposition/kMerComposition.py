# -*- coding:utf-8 -*-
from collections import Counter
import itertools
from Bio.Seq import Seq
from Bio import SeqIO
'''
https://rosalind.info/problems/kmer/
'''

def main():
    cdict = {}
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        a = str(record_dict[k].seq)
    for i in range(len(a)-4+1):
        kmer = a[i:i+4]
        if kmer not in cdict:
            cdict[kmer] = 1
        else:
            cdict[kmer] += 1

    b = Counter(a)
    c = list(b.keys())

    klist = []
    for i in itertools.product(c, repeat = 4):
        klist.append(''.join(i))
    klist = sorted(klist)
    rlist = []
    for i in klist:
        if i in cdict:
            rlist.append(str(cdict[i]))
        else:
            rlist.append('0')
    print(" ".join(rlist))




if __name__ == "__main__":
    main()

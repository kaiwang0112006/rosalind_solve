# -*- coding:utf-8 -*-
from Bio import SeqIO
from Bio.Seq import Seq
import collections
import copy

'''
problem: http://rosalind.info/problems/splc/
'''

def main():
    with open("example.fasta") as handle:
        count = 0
        for record in SeqIO.parse(handle, "fasta"):
            if count==0:
                mainseq = str(record.seq)
            else:
                mainseq = mainseq.replace(str(record.seq), ' ')
            count+=1
    exons = mainseq.split(' ')

    result = ''
    for e in exons:
        result+=Seq(e).translate()
    print(result)
    
if __name__ == "__main__":
    main()

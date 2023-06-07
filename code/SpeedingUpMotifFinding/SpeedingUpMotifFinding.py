# -*- coding:utf-8 -*-
from Bio import SeqIO
from Bio.Seq import Seq
import collections
import copy
import numpy as np
import re
'''
problem: https://rosalind.info/problems/kmp/
'''


def main_bak():
    '''
    bug
    :return:
    '''
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        s = str(record_dict[k].seq)

    firsts = s[0]
    tl = len(s)
    rlist = [0 for i in range(tl)]
    for i in range(1, tl):
        if s[i] == firsts:
            if rlist[i]<1:
                rlist[i] = 1
            if i!=tl-1 and i!=1:
                for j in range(1,tl-i+1):
                    if s[i:i+j] == s[:j]:
                        if rlist[i + j - 1] < j:
                            rlist[i+j-1] = rlist[i+j-1]+1
                    else:
                        break
    print(" ".join([str(i) for i in rlist]))
    
def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        dna = str(record_dict[k].seq)
    flag = True
    farr = np.zeros(len(dna), dtype=np.int32)

    i = 1
    while flag:
        print(i)
        mat = re.finditer("(?=(%s))" % dna[:i], dna[1:])

        flag = False
        for m in mat:
            idx = m.end(1)
            farr[idx] = len(dna[:i])
            #print(dna[:i],dna[idx-i+1:idx+1])
            flag = True

        i += 1
    
    print(" ".join([str(i) for i in farr]))

if __name__ == "__main__":
    main()

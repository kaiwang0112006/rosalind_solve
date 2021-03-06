# -*- coding:utf-8 -*-
from Bio import SeqIO
import collections
import copy

'''
problem: http://rosalind.info/problems/grph/
'''

def lcs(S,T):
    #print(S,T)
    #print(type(S), type(T))
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
    #print(lcs_set)
    return lcs_set, longest

def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    idlist = list(record_dict.keys())
    com, l = lcs(str(record_dict[idlist[0]].seq),str(record_dict[idlist[1]].seq))

    for i in range(2, len(idlist)):
        comdict = {}
        for sq in com:
            com_sub, l = lcs(sq,str(record_dict[idlist[i]].seq))
            comdict[l] = com_sub
        com = comdict[max(comdict.keys())]

    print(com)

if __name__ == "__main__":
    main()
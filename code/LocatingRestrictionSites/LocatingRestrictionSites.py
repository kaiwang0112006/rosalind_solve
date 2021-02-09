# -*- coding:utf-8 -*-
from Bio.Seq import Seq
from Bio import SeqIO

'''
problem: http://rosalind.info/problems/revp/
'''

def isPalindrome(s):
    s = s.upper()
    sv = s[::-1]
    smap = {"A":"T","T":"A","C":"G","G":"C"}
    #print(sv)
    #sv = sv.translate(str.maketrans('ACGT', 'TGCA'))
    sv = ''.join([smap[i] for i in sv])
    #print(sv,s)
    return sv == s

def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        seq = record_dict[k].seq
    for i in range(len(seq)-3):
        lmax = min(len(seq[i:]),12)
        for ll in range(4,lmax+1):
            subseq = seq[i:i+ll]
            if isPalindrome(subseq):
                print(i+1,ll)

def main_fast():
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        seq = record_dict[k].seq
    for i in range(len(seq)-3):
        lmax = min(len(seq[i:]),12)
        if lmax % 2 !=0:
             lmax = lmax+1
        for ll in range(4,lmax+1,2):
            subseq = seq[i:i+ll]
            if isPalindrome(subseq):
                print(i+1,ll)

if __name__ == "__main__":
    main()

# -*- coding:utf-8 -*-
from Bio.Seq import Seq
from Bio import SeqIO
import re

def main():
    rlist = []
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    for k in record_dict:
        for st in range(3):
            s = record_dict[k].seq[st:].translate()
            #print(s)
            for aa in re.findall(r"(?=(M[A-Z]*\*))",str(s)):
                rlist.append(aa[:-1])
            s = record_dict[k].reverse_complement().seq[st:].translate()
            #print(s)
            for aa in re.findall(r"(?=(M[A-Z]*\*))",str(s)):
                rlist.append(aa[:-1])
    for s in set(rlist):
        print(s)

if __name__ == "__main__":
    main()

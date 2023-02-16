# -*- coding:utf-8 -*-

from Bio import SeqIO
import collections

def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("gcexample.fasta", "fasta"))
    c = 0
    r = ''
    for id in record_dict:
        obj = collections.Counter(record_dict[id])
        gc = (obj['C'] +obj['G'])/len(record_dict[id])
        gc = gc*100
        if gc>c:
            c = gc
            r = id
    print(r,c)

if __name__ == "__main__":
    main()
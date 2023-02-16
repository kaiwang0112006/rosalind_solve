# -*- coding:utf-8 -*-

from Bio import SeqIO
import collections
import copy

def mainbak():
    record_dict = SeqIO.to_dict(SeqIO.parse("example1.fasta", "fasta"))
    seqlist = [record_dict[id] for id in record_dict]
    pmat = []
    for i in range(len(seqlist[0])):
        obj = collections.Counter([s[i] for s in seqlist])
        cmap = {}
        for k in ['A','T','C','G']:
            cmap[k] = obj[k]
        pmat.append(cmap)
    consensuslist = ['']
    for m in pmat:
        mv = max(m.values())
        ks = []
        for k in m:
            if m[k] == mv:
                ks.append(k)

        consensusbak = []
        for i in range(len(consensuslist)):
            consensusstr = consensuslist[i]
            for k in ks:
                consensusbak.append(consensusstr+k)
        consensuslist = copy.deepcopy(consensusbak)

    for s in consensuslist:
        print(s)

    for j in ['A','C','G','T']:
        jstr = j +":"
        for m in pmat:
            jstr += " %s" % m[j]
        print(jstr)

def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("example1.fasta", "fasta"))
    seqlist = [record_dict[id] for id in record_dict]
    pmat = []
    for i in range(len(seqlist[0])):
        obj = collections.Counter([s[i] for s in seqlist])
        cmap = {}
        for k in ['A','T','C','G']:
            cmap[k] = obj[k]
        pmat.append(cmap)
    consensuslist = ''
    for m in pmat:
        vl = sorted(list(m.keys()), key=lambda x: m[x], reverse=True)

        consensuslist = consensuslist+vl[0]
    print(consensuslist)
    for j in ['A','C','G','T']:
        jstr = j +":"
        for m in pmat:
            jstr += " %s" % m[j]
        print(jstr)





if __name__ == "__main__":
    main()
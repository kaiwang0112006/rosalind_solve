# -*- coding:utf-8 -*-
from Bio import SeqIO

def pdistance(s,t):
    assert len(s)==len(t)
    assert len(s)>0

    difnum = 0
    for i in range(len(s)):
        if s[i]!=t[i]:
            difnum += 1
    return round(difnum/len(s),5)


def main():
    seq_list = []
    handle = open('sampledata.fasta', 'r')
    for record in SeqIO.parse(handle, 'fasta'):
        sequence = str(record.seq)
        seq_list.append(sequence)

    sl = len(seq_list)
    for i in range(sl):
        linestr = ""
        for j in range(sl):
            dis = pdistance(seq_list[i], seq_list[j])
            disstr = "{:.5f}".format(dis)
            linestr += disstr + " "
        #linestr[-1] = ""
        print(linestr)


if __name__ == "__main__":
    main()
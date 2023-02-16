# -*- coding:utf-8 -*-
from Bio import SeqIO
from io import StringIO

'''
problem: http://rosalind.info/problems/long/
'''

def findoverlap(s1,s2,reverse_op=False):
    '''
    parms: s1=ATTAGACCTG, s2=CCTGCCGGAA
    reverse_op=False 时返回 CCTG
    reverse_op=True 时返回 A
    '''
    if reverse_op:
        s1, s2 = s2, s1

    l = min(len(s1),len(s2))
    while s1[-1*l:] != s2[:l]:
        #print('findoverlap', l, s1[-1*l:],s2[:l])
        l -=1
        if l==0:
            break
    if l == 0:
        return ''
    else:
        return s1[-1*l:]

def findoverlap_bak(s1,s2,reverse_op=False):
    if reverse_op:
        s1, s2 = s2, s1
    temp = (i for i in range(len(s2), 0, -1) if s2[:i] == s1[-i:])
    temp2 = next(temp, 0)
    return s2[:temp2]

def glue(sl):
    maxl = 0
    overlap = ''
    org = ''
    ind = None
    st = sl[0]
    for i in range(1,len(sl)):
        overlap1 = findoverlap(st,sl[i],reverse_op=False)
        overlap2 = findoverlap(st,sl[i],reverse_op=True)

        if len(overlap1)>len(overlap2) and len(overlap1)>maxl:
            maxl = len(overlap1)
            overlap = overlap1
            org = False
            ind = i
        elif len(overlap2)>=len(overlap1) and len(overlap2)>maxl:
            maxl = len(overlap2)
            overlap = overlap2
            org = True
            ind = i
        #print(st, sl[i], overlap1, overlap2,org)

    if org == True:
        comb = sl[ind] + st.replace(overlap,'')
    elif org == False:
        comb = st + sl[ind].replace(overlap,'')
    sed = sl[ind]
    sl = [i for i in sl if i not in [st, sed]]

    return [comb] + sl


def main():
    record_dict = SeqIO.to_dict(SeqIO.parse("example.fasta", "fasta"))
    seqlist = []
    for k in record_dict:
        seqlist.append(str(record_dict[k].seq))

    while len(seqlist) >1:
        seqlist = glue(seqlist)
    seqglue = seqlist[0]
    print(seqglue)
    with open('result.txt','w') as f:
        f.write(seqglue)


if __name__ == "__main__":
    main()

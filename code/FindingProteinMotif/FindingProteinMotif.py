# -*- coding:utf-8 -*-
import requests
from Bio import SeqIO
from io import StringIO
import re

'''
problem: http://rosalind.info/problems/mprt/
'''

def getRE_result(seqs, query):
    '''
    :param seqs: protein seqence.
    :param query: search pattern in regular expression.
    :return: list that contain all start position.
    '''

    ms = [str(m.start() + 1) for m in re.finditer(query, seqs)]
    return ms

def main():
    inputstr = '''
P20268
Q5WFN0
P02974_FMM1_NEIGO
P22457_FA7_BOVIN
P01189_COLI_HUMAN
P19823_ITH2_HUMAN
P07359_GPBA_HUMAN
P36913_EBA3_FLAME
Q4FZD7
P05783_K1CR_HUMAN
P21810_PGS1_HUMAN
B8GYE3
Q8WW18
    '''
    query = r'(?=(N[^P](S|T)[^P]))'
    inputlist = inputstr.split()
    baseUrl = "http://www.uniprot.org/uniprot/"
    for i in range(len(inputlist)):
        cID = inputlist[i]
        currentUrl = baseUrl + cID + ".fasta"
        response = requests.post(currentUrl)
        cData = ''.join(response.text)
        Seq = StringIO(cData)
        pSeq = SeqIO.to_dict(SeqIO.parse(Seq, 'fasta'))
        msall = []
        for k in pSeq:
            seqs = str(pSeq[k].seq)
            ms = getRE_result(seqs, query)
            msall = msall+ms
        if len(msall)>0:
            print(cID)
            print(' '.join(msall))



if __name__ == "__main__":
    main()
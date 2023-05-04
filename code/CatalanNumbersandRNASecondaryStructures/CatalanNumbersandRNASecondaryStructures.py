from Bio import SeqIO
from math import factorial

def ispair(a, b):
    if a == "A" and b == "U":
        return True
    elif a == "U" and b == "A":
        return True
    elif a == "G" and b == "C":
        return True
    elif a == "C" and b == "G":
        return True
    else:
        return False


def catalan(dna, cata):
    if dna in cata:
        return cata[dna]
    n = len(dna)
    c=0
    for m in range(1, n, 2):
        if ispair(dna[0], dna[m]):
            c += (catalan(dna[1:m], cata) * catalan(dna[m+1:], cata))
    cata[dna] = c
    return cata[dna]

def main():
    sequence = ''
    handle = open('sampledata.fasta', 'r')
    for record in SeqIO.parse(handle, 'fasta'):
        sequence = str(record.seq)
    handle.close()
    cata = {'': 1, 'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1}
    print(catalan(sequence, cata) % 1000000)


if __name__ == "__main__":
    main()
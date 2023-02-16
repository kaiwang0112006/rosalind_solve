from Bio import SeqIO
from math import factorial

def main():
    sequence = ''
    handle = open('sampledata.fasta', 'r')
    for record in SeqIO.parse(handle, 'fasta'):
        sequence = str(record.seq)
    handle.close()

    AU = 0
    GC = 0
    for nt in sequence:
        if nt == 'A':
            AU += 1
        elif nt == 'G':
            GC += 1

    matchings = factorial(AU) * factorial(GC)
    print(matchings)

if __name__ == "__main__":
    main()
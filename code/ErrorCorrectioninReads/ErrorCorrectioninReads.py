from Bio import SeqIO

def hammingDist(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

#只对正确序列求反比对

def main():
    sequences_count = {}
    seqmap = {}
    seqmap_r = {}
    # fasta parser
    handle = open('sampledata.fasta', 'r')
    for record in SeqIO.parse(handle, 'fasta'):
        orgseq = str(record.seq)
        reverseseq = str(record.reverse_complement().seq)
        seqmap[orgseq] = reverseseq
        seqmap[reverseseq] = orgseq

        if reverseseq in sequences_count:
            sequences_count[reverseseq] += 1
        elif orgseq in sequences_count:
            sequences_count[orgseq] += 1
        else:
            sequences_count[orgseq] = 1

    # separate correct and incorrect
    correct_seqs = []
    incorrect_seqs = []
    for s in sequences_count:
        if sequences_count[s] == 1:
            incorrect_seqs.append(s)
        else:
            correct_seqs.append(s)

    # cal error reads
    for i in range(len(incorrect_seqs)):
        for j in range(len(correct_seqs)):
            seq1 = incorrect_seqs[i]
            seq2 = correct_seqs[j]
            seq3 = seqmap[seq2]
            if hammingDist(seq1, seq2) == 1:
                seqorder = sorted([seq1, seq2])
                seqmap_r[tuple(seqorder)] = [seq1, seq2]
            elif hammingDist(seq1, seq3) == 1:
                seqorder = sorted([seq1, seq3])
                seqmap_r[tuple(seqorder)] = [seq1, seq3]

    for tu in seqmap_r:
        print("%s->%s" % (seqmap_r[tu][0],seqmap_r[tu][1]))

if __name__ == "__main__":
    main()
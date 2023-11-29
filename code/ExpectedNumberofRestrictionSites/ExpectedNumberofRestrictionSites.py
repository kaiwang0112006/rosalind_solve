# -*- coding:utf-8 -*-
import math
import scipy.special

def main():
    data = []
    with open('rosalind_prob.txt', 'r') as f:
        for line in f:
            data.append(line.strip('\n'))
    n = int(data[0])
    s = data[1]
    A = [float(x) for x in data[2].split()]

    AT, GC = 0, 0
    for nt in s:
        if nt == 'A' or nt == 'T':
            AT += 1
        elif nt == 'G' or nt == 'C':
            GC += 1

    B = [None] * len(A)
    for i, j in enumerate(A):
        P = (((1 - j) / 2) ** AT) * ((j / 2) ** GC) * (n - len(s) + 1)
        B[i] = '%0.3f' % P
    print(*B, sep=' ')


if __name__ == "__main__":
    main()
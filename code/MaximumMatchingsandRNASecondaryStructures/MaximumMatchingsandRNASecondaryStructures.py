# -*- coding:utf-8 -*-

from collections import Counter
from math import factorial


def main():
    seq = "AAAGGCUUGGAUUGUCAUACUUGUUAAGGCAUCGUAGGCGGCAGUCCGGAAGGUAACGAACUGGUCGAGGACGUACUCCCAGAGUGGAGAU"

    A = seq.count('A')
    U = seq.count('U')
    C = seq.count('C')
    G = seq.count('G')
    print(A,U,C,G)
    GCmax = max(G, C)
    GCmin = min(G, C)
    AUmax = max(A, U)
    AUmin = min(A, U) # 把每一对中较大的和较小的分出来

    MMAU = factorial(AUmax)//factorial(AUmax-AUmin)
    MMGC = factorial(GCmax)//factorial(GCmax-GCmin)
    num = MMAU*MMGC

    print(num)


if __name__ == "__main__":
    main()
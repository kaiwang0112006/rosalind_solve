# -*- coding:utf-8 -*-
from collections import *
import itertools

def main():
    n = 3
    alphabet = 'Q O E W'.replace(" ","")
    perm = []
    for i in range(1, n + 1):
        perm.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))
    permutations = list(itertools.chain(*perm))
    srt_perm = sorted(permutations,key=lambda word: [alphabet.index(c) for c in word])
    with open("r.txt",'w') as f:
        r = '\n'.join(srt_perm)
        f.write(r)



if __name__ == "__main__":
    main()
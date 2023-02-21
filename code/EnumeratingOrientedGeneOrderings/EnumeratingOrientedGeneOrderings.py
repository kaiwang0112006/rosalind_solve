# -*- coding:utf-8 -*-
from itertools import *
import copy
def main():
    n = 2
    dlist = []
    for prod in (product(*[(-i, i) for i in p]) for p in permutations(range(1, n + 1))):
        for perm in prod:
            dlist.append([str(j) for j in perm])
    print(len(dlist))
    for d in dlist:
        print(" ".join(d))

if __name__ == "__main__":
    main()
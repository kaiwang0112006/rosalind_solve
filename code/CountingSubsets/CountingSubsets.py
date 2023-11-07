# -*- coding:utf-8 -*-
import itertools
import numpy as np
import math

def main():
    n = 847
    if n ==1:
        print(1)
    else:
        num = 1
        for i in range(n):
            comb = math.comb(n, i+1)
            num += comb
        print(num%1000000)





if __name__ == "__main__":
    main()
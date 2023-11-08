# -*- coding:utf-8 -*-
import math

def main():
    n = 1846
    m = 688
    num = 0
    for i in range(m,n+1):
        comb = math.comb(n, i)
        num += comb
    print(num%1000000)





if __name__ == "__main__":
    main()
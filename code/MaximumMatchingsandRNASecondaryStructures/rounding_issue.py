# -*- coding:utf-8 -*-
import numpy as np
from functools import reduce
from math import factorial

def main():
    n = 23
    m = 3

    # cal by details to avoid rounding issue
    r = [i for i in range(n,m,-1)]

    rr = reduce(lambda x, y: x*y, r)
    print(f"cal by details to avoid rounding issue: {rr}")

    # cal by factorial method
    rr = int(factorial(n)/factorial(m))
    print(f"cal by factorial method: {rr}")

    # cal by factorial method with floor division
    rr = int(factorial(n)//factorial(m))
    print(f"cal by factorial method with floor division: {rr}")




if __name__ == "__main__":
    main()
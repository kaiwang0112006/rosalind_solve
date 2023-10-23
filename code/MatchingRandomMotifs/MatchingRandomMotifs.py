# -*- coding:utf-8 -*-
import math
def main():
    num = 98037
    seq = "GTACTCGAC"
    cgprob = 0.474973

    logarithm = 1
    probmap = {}
    probmap["A"] = (1 - cgprob) / 2
    probmap["T"] = (1 - cgprob) / 2
    probmap["C"] = cgprob / 2
    probmap["G"] = cgprob / 2
    for s in seq:
        s = s.upper()
        logarithm = logarithm*probmap[s]
        #logarithm += math.log(probmap[s],10)
    result = 1-(1-logarithm)**num
    print(result)


if __name__ == "__main__":
    main()

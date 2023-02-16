# -*- coding:utf-8 -*-
import math

def main():
    with open(r"E:\work\github\rosalind_solve\code\IntroductiontoRandomStrings\rosalind_prob.txt") as f:
        data = f.readlines()
    seq = data[0].strip()
    problist = [float(i) for i in  data[1].split()]
    print(seq)
    print(problist)
    probRecord = []
    for i, p in enumerate(problist):
        logarithm = 0
        probmap = {}
        probmap["A"] = (1 - problist[i]) / 2
        probmap["T"] = (1 - problist[i]) / 2
        probmap["C"] = problist[i] / 2
        probmap["G"] = problist[i] / 2
        for s in seq:
            s = s.upper()
            logarithm += math.log(probmap[s],10)
        probRecord.append(str(logarithm))
    print(" ".join(probRecord))


if __name__ == "__main__":
    main()
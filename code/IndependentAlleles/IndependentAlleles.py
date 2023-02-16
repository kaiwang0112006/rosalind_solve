# -*- coding:utf-8 -*-
from itertools import combinations
import collections
from scipy.special import binom
'''
problem: http://rosalind.info/problems/lia/
'''

def getsubtype(s):
    '''
    :param s: "AaBb"
    :return: ["AB","Ab","aB","ab"]
    '''
    l1 = [s[0],s[1]]
    l2 = [s[2],s[3]]
    rl = []
    for i in l1:
        for j in l2:
            rl.append(i+j)
    return rl

def Mendel(S,T):
    sub1 = getsubtype(S)
    sub2 = getsubtype(T)
    comb = []
    #print(S,sub1,T,sub2)
    for i in sub1:
        for j in sub2:
            comb.append(min(i[0],j[0])+max(i[0],j[0])+min(i[1],j[1])+max(i[1],j[1]))
    cb = dict(collections.Counter(comb))
    sumv = sum(cb.values())
    for k in cb:
        cb[k] = cb[k]/sumv
    return cb

def calAa(k):
    if k==0:
        return Mendel("AaBb","AaBb")
    else:
        pdict = calAa(k-1)
        gentypes = list(pdict.keys())
        rlist = {}
        for t in pdict:
            rdict = Mendel(t,"AaBb")
            #print(t,"AaBb",rdict)
            rlist[(t,"AaBb")] = rdict
            gentypes = gentypes+list(rdict.keys())
        returnrtpes = {}
        for t in set(gentypes):
            returnrtpes[t] = 0
            for g in pdict:
                returnrtpes[t] += pdict[g]*rlist[(g,"AaBb")].get(t,0)
        #print(k, returnrtpes)
        return returnrtpes

def test():
    print(Mendel("AaBb", "AaBb"))

def solution_by_me():
    k = 2
    N = 1
    pdict = calAa(k)
    pr = 0
    print(pdict)
    for n in range(N,(2**k)+1):
        up = len(list(combinations(list(range(2**k)), n)))
        pr += up*(pdict['AaBb']**n)*((1-pdict['AaBb'])**(2**k-n))
    print(pr)

def solution_from_web():

    def foo(k, N):
        def p(n, k):
            return binom(2 ** k, n) * 0.25 ** n * 0.75 ** (2 ** k - n)

        for n in range(N, 2 ** k + 1):
            print(n, p(n, k),binom(2 ** k, n))
        return sum(p(n, k) for n in range(N,2**k+1))
        #return 1 - sum(p(n, k) for n in range(N))

    print(round(foo(2, 1), 3))

def main():
    solution_by_me()

if __name__ == "__main__":
    main()

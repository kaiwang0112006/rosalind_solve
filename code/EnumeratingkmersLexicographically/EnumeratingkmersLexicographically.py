# -*- coding:utf-8 -*-
import itertools

'''
http://rosalind.info/problems/lexf/
'''

def main_org():
    a = 'A C G T'.replace(' ','')
    rlist = []
    for i in itertools.permutations(a+a, 2):
        rlist.append(''.join(i))
    rlist = sorted(list(set(rlist)))
    for i in rlist:
        print(i)

def main():
    a = 'A B C D'.replace(' ','')
    rlist = []
    for i in itertools.product(a, repeat = 4):
        rlist.append(''.join(i))
    rlist = sorted(list(set(rlist)))
    for i in rlist:
        print(i)

if __name__ == "__main__":
    main()

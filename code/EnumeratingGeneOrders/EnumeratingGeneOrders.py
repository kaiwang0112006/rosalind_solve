# -*- coding:utf-8 -*-
import itertools

def main():
    n = 7
    iobjlist = list(itertools.permutations([str(i) for i in range(1,n+1)]))
    fout = open('result','w')
    fout.write(str(len(iobjlist))+'\n')
    for ex in iobjlist:
        fout.write(' '.join(ex))
        fout.write('\n')
    fout.close()

if __name__ == "__main__":
    main()

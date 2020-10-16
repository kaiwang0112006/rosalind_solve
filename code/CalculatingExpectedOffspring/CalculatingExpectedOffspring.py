# -*- coding:utf-8 -*-


'''
problem: http://rosalind.info/problems/iev/
'''

def main():
    s = '19649 18991 17249 18533 19874 16390'
    a1,a2,a3,a4,a5,a6 = [int(i) for i in s.split(' ')]

    print((a1+a2+a3+0.75*a4+0.5*a5)*2)

if __name__ == "__main__":
    main()
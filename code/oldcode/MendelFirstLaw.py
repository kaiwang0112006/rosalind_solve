# -*- coding:utf-8 -*-

'''
so disscusion: https://stackoverflow.com/questions/25119106/rosalind-mendels-first-law-iprb

'''
def main():
    k = 2
    m = 2
    n = 2

    ac = k+m+n
    r = k/ac*m/(ac-1)*2+k/ac*(k-1)/(ac-1)+k/ac*n/(ac-1)*2+m/ac*n/(ac-1)+m/ac*(m-1)/(ac-1)*3/4
    r = k/ac*(k-1)/(ac-1)+k/ac*m/(ac-1)*2+k/ac*n/(ac-1)*2+m/ac*(m-1)/(ac-1)*3/4+m/ac*n/(ac-1)*1/2*2
    print(r)

if __name__ == "__main__":
    main()
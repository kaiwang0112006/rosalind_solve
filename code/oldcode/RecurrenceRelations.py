# -*- coding:utf-8 -*-


def main():
    n=3
    k=2

    i = 2
    adult = 1
    young = 0
    while i<n:
        i+= 1
        newyoung = adult*k
        adult += young
        young = newyoung

    print(adult,young, i)

def solution2():
    '''
    斐波那契的兔子，f1正好等于下一轮要繁殖的兔子，因此f1需要乘以繁殖个数，f2是下一轮的成年兔子数
    :return:
    '''
    n=5
    k=3

    f1 = 1
    f2 = 1
    i= 2
    while i<n:
        f1, f2 = f2, f1*k+f2
        i+=1

    print(f2,i)

if __name__ == "__main__":
    solution2()
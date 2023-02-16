# -*- coding:utf-8 -*-

def fib(n, m):
    if n == 1:
        return 1
    elif n <=0:
        return 0
    elif n==2:
        return 1
    elif n<=m:
        return fib(n - 1, m) + fib(n - 2, m)
    elif n == m+1:
        return fib(n - 1, m) + fib(n - 2, m)-1
    else:
        a = fib(n-1,m)
        b = fib(n-2,m)
        c = fib(n-m-1,m)

        return a+b-c

def fibonacciRabbits(n, m):
    F = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = F[i - 1] + F[i - 2]
        elif i == m + 1:
            total = F[i - 1] + F[i - 2] - 1
        else:
            total = F[i - 1] + F[i - 2] - F[i - m - 1]
        F.append(total)
    return (F[n])

def solv_try(n,m):

    total = [0]
    for i in range(n):
        for i in range(len(total)):
            total[i] = total[i]+1
            if total[i] >2:
                total.append(1)
        total = [f for f in total if f<=m]
        print(total)
    return len(total)


def main():
    print(solv_try(6,3))

if __name__ == "__main__":
    main()
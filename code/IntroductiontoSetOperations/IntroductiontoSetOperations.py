# -*- coding: utf-8 -*-

def main():
    n = 10
    a = set({1, 2, 3, 4, 5})
    b = set({2, 8, 5, 10})
    c = set(range(1,n+1))

    print(a | b)
    print(a & b)
    print(a-b)
    print(b-a)
    print(c-a)
    print(c-b)

if __name__ == "__main__":
    main()
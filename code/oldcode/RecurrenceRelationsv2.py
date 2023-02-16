# -*- coding:utf-8 -*-

def fab(n,k):
    if n<=2:
        return 1
    else:
        return fab(n-1,k)+fab(n-2,k)*k

def main():
    n=5
    k=3
    print(fab(n,k))


if __name__ == "__main__":
    main()
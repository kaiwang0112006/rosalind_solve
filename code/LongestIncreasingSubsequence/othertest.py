# -*- coding:utf-8 -*-
import timeit
import copy

def bisect_ascending(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisect_descending(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] > x: lo = mid+1
        else: hi = mid
    return lo

def longest_increasing_subsequence(seq, n):
    tops = []
    links = {}

    for elem in seq:
        i = bisect_ascending(tops, elem)
        if i == len(tops):
            tops.append(elem)
        else:
            tops[i] = elem
        links[elem] = tops[i - 1] if i > 0 else None

    lisubseq = [tops[-1]]
    while links[lisubseq[-1]]:
        lisubseq.append(links[lisubseq[-1]])

    lisubseq.reverse()
    return lisubseq

def longest_decreasing_subsequence(seq):
    tops = []
    links = {}

    for elem in seq:
        i = bisect_descending(tops, elem)
        if i == len(tops):
            tops.append(elem)
        else:
            tops[i] = elem
        links[elem] = tops[i - 1] if i > 0 else None
        #print(elem, i, tops, links)

    ldsubseq = [tops[-1]]
    while links[ldsubseq[-1]]:
        ldsubseq.append(links[ldsubseq[-1]])

    ldsubseq.reverse()
    return ldsubseq

def lis_3(x,reverse_item=True):
    '''
    可以适应重复元素，效率相应降低
    '''
    N = len(x)
    subseq = []
    for i in range(N):
        if i == 0:
            subseq.append([x[i]])
        else:
            for subi in range(len(subseq)):
                if reverse_item:
                    choose = x[i]<=subseq[subi][-1]
                else:
                    choose = x[i]>=subseq[subi][-1]
                if choose:
                    newarr = copy.deepcopy(subseq[subi])
                    newarr.append(x[i])
                    subseq.append(newarr)
            subseq.append([x[i]])

    longth = 0
    ans = None
    for i in subseq:
        if len(i)>longth:
            longth = len(i)
            ans = i
    return ans
    #return set([tuple(i) for i in subseq])

def main():
    a = [5,6,4,2,9,4,3,1]
    print(timeit.timeit("longest_decreasing_subsequence(%s)" % str(a), setup="from __main__ import longest_decreasing_subsequence"))
    print(timeit.timeit("lis_3(%s)" % str(a), setup="from __main__ import lis_3"))
    #print(lis_3(a))

if __name__ == "__main__":
    main()

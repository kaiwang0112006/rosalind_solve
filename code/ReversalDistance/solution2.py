import collections
import time
import copy

def get_all_permutations(s):
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            yield s[:i] + s[i:j][::-1] + s[j:]


def get_reversal_distance(p1, p2):
    distance = 0
    if p1 == p2:
        return distance

    cands = {p2: 0}
    cands_list = list(cands.keys())
    cands_list_record = []
    cands_list_record_all = {}
    while True:
        for s in cands_list:
            for j in get_all_permutations(s):
                if j == p1:
                    return distance + 1
                else:
                    if j not in cands_list_record_all:
                        cands_list_record.append(j)
                        cands_list_record_all[j] = 1
        cands_list = copy.deepcopy(cands_list_record)
        cands_list_record = []
        distance += 1

def main():
    inputfile = "input.txt"

    with open(inputfile) as fp:
        r=fp.read().split('\n')
        r=[tuple(r[i].split())for i in range(len(r)) if r[i]!='']

    result = [get_reversal_distance(r[i],r[i+1]) for i in range(0,len(r)-1,2)]
    print(result)


if __name__ == "__main__":
    main()
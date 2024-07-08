# -*- coding:utf-8 -*-

import random

# get the all reversal array of a list "s".
def _get_reverse_array(s):
    '''
    Parameters
    ----------
    s: 输入数组, 如 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Returns
    -------
    reverse_arrays: [[2, 1, 3, 4, 5, 6, 7, 8, 9, 10], [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]...]
    所有元素下标对应的反转数组，如 1,3反转得到 [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], 1,4反转得到 [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]...
    '''
    reverse_arrays = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            r_list = s[i:j + 1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j + 1:])

    return reverse_arrays


# get the reversal_distance from a list "s1" to another list "s2".
def _get_reversal_distance(s1, s2, distance, s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals):
    # reverse s1 to s2, and reverse s2 to s1 at same time.
    if s1 & s2:
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance
    # get the reveral array of s1.
    new_s1 = set()
    s1_s2 = {}
    for s in s1:
        reverse_arrays = _get_reverse_array(list(s))
        s1_s2[s] = reverse_arrays
        for r in reverse_arrays:
            new_s1.add(tuple(r))
    s1_s2_reversals_path.append(s1_s2)
    # get the reveral array of s2.
    new_s2 = set()
    s2_s1 = {}
    for s in s2:
        reverse_arrays = _get_reverse_array(list(s))
        s2_s1[s] = reverse_arrays
        for r in reverse_arrays:
            new_s2.add(tuple(r))
    s2_s1_reversals_path.append(s2_s1)
    # thus we reverse s1 and s2 at same time, so distance plus 2.
    distance += 2
    # if s1 and the reversal array of s2 has the same array, distance substract 1.
    if s1 & new_s2:
        meet_reversals = list(s1 & new_s2)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance - 1
    # if s2 and the reversal array of s1 has the same array, distance substract 1.
    if s2 & new_s1:
        meet_reversals = list(s2 & new_s1)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance - 1
    # if reversal array of s1 and the reversal array of s2 has the same array, return distance.
    if new_s1 & new_s2:
        meet_reversals = list(new_s1 & new_s2)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance

    s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance = _get_reversal_distance(new_s1, new_s2,
                                                                                                  distance,
                                                                                                  s1_s2_reversals_path,
                                                                                                  s2_s1_reversals_path,
                                                                                                  meet_reversals)
    return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance


# get the endpoints of the interval of the two indices.
def _get_invert_endpoints(a, b):
    a_reverse = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            a_reverse = a[:i] + a[i:j + 1][::-1] + a[j + 1:]
            if a_reverse == b:
                return i + 1, j + 1


# get the collections of reversals sorting π into γ
def _get_collections_of_reversals_sorting(s1_s2_reversals_path, meet_reversals, s2_s1_reversals_path):
    collections_of_reversals_sorting = []
    for l in meet_reversals:
        # print(l)
        collection_of_reversals_sorting = []
        current_array = list(l)
        for reversals_path in s1_s2_reversals_path[::-1]:
            for k, v in reversals_path.items():
                if current_array in v:
                    i, j = _get_invert_endpoints(list(k), current_array)
                    collection_of_reversals_sorting.append([i, j])
                    current_array = list(k)
                    break
        collection_of_reversals_sorting = collection_of_reversals_sorting[::-1]
        current_array = list(l)
        for reversals_path in s2_s1_reversals_path[::-1]:
            for k, v in reversals_path.items():
                if current_array in v:
                    i, j = _get_invert_endpoints(list(k), current_array)
                    collection_of_reversals_sorting.append([i, j])
                    current_array = list(k)
                    break
        collections_of_reversals_sorting.append(collection_of_reversals_sorting)
    return collections_of_reversals_sorting


if __name__ == "__main__":
    # test
    #a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #b = [1, 8, 9, 3, 2, 7, 6, 5, 4, 10]
    # load data
    with open("rosalind_sort.txt", "r") as f:
        a = [int(i) for i in f.readline().strip().split(" ")]
        b = [int(i) for i in f.readline().strip().split(" ")]

    # main solution
    distance, s1, s2 = 0, set(), set()
    s1.add(tuple(a)), s2.add(tuple(b))
    s1_s2_reversals_path = []  # the list contains reversals path (dict) from s1 to s2.
    s2_s1_reversals_path = []  # the list contains reversals path (dict) from s2 to s1.
    meet_reversals = []  # the reversals met by s1-s2 direction and s2-s1 direction.
    s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance = _get_reversal_distance(s1, s2, distance,
                                                                                                  s1_s2_reversals_path,
                                                                                                  s2_s1_reversals_path,
                                                                                                  meet_reversals)  # 4
    print("[INFO] the distance of reverse s1 to s2: {}".format(distance))
    # print(s1_s2_reversals_path)
    # print(s2_s1_reversals_path)
    # print(meet_reversals)

    collections_of_reversals_sorting = _get_collections_of_reversals_sorting(s1_s2_reversals_path, meet_reversals,
                                                                             s2_s1_reversals_path)
    print("[INFO] the number of collections of reversals sorting π into γ: {}".format(
        len(collections_of_reversals_sorting)))
    a_collection = random.sample(collections_of_reversals_sorting, k=1)[0]
    print("[INFO] the reversal distance drev(π,γ): {}".format(len(a_collection)))
    print("A random collection of reversals sorting π into γ:")
    print(a_collection)
    print("format output:")
    print(len(a_collection))
    for output in a_collection:
        print(" ".join([str(i) for i in output]))
    #print(a_collection)
    print("done!")
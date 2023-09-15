## [Reversal Distance](https://rosalind.info/problems/rear/)

### 背景知识

**翻转距离(reversal distance)**: 序列反转是指染色体发生断裂后，某一区段颠倒180度后重新连接。字符串的翻转距离是指从一个字符串转变为另一个字符串
所需要的最小的翻转次数。

### 问题

给定：一组最多5对数字排列，排列长度为10

输出：，每对排列的翻转距离

示例输入: 

    1 2 3 4 5 6 7 8 9 10
    3 1 5 2 7 4 9 6 10 8
    
    3 10 8 2 5 4 7 1 6 9
    5 2 3 1 7 4 10 8 6 9
    
    8 6 7 9 4 1 3 10 2 5
    8 2 7 6 9 1 5 3 10 4
    
    3 9 10 4 1 8 6 7 5 2
    2 9 8 5 1 7 3 4 6 10
    
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10

示例出: 

    9 4 5 7 0

###  解决

一种解决方法是枚举一个序列所有的一次翻转，判断是否能得到另一个序列，然后对所有的一次翻转继续枚举。

枚举所有一次翻转的方法：

    def get_all_permutations(s):
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                yield s[:i] + s[i:j][::-1] + s[j:]

判断是否能得到另一个序列：

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

文件读取：

    def main():
        inputfile = "input.txt"
    
        with open(inputfile) as fp:
            r=fp.read().split('\n')
            r=[tuple(r[i].split())for i in range(len(r)) if r[i]!='']
    
        result = [get_reversal_distance(r[i],r[i+1]) for i in range(0,len(r)-1,2)]
        print(result)

从别人的例子里还能得到一种优化的方法，见[rear.py](https://github.com/fernandoBRS/Rosalind-Problems/blob/master/rear.py)。
实际上是从两头出发，因为一侧枚举可能到后面计算量越来越大。因此，控制从序列1开始枚举5次后，就从序列2开始枚举，步数取两头枚举次数的加和。

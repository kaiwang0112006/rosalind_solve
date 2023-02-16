## [Enumerating k-mers Lexicographically](http://rosalind.info/problems/lexf/)

### 背景知识

字典序排序: 两个长度都是n的字符串s, t的字典序排序指s和t的第一个不相同的字符s[i]<t[i]

### 问题

给定：一个字符集和一个正整数n

输出：所有可以从这个字符集定义的长度为n的子字符串，按字典序排序

### 解决

分两步，第一步利用排列组合找到所有输出的字符串集，第二步按字典序排序，因为python默认的sort函数可以解决，没有再另构建字典序排序函数。

    def main():
        a = 'A B C D'.replace(' ','')
        rlist = []
        for i in itertools.product(a, repeat = 4):
            rlist.append(''.join(i))
        rlist = sorted(list(set(rlist)))
        for i in rlist:
            print(i)

### 扩展

当对得到的大量遗传学相关的字符串（DNA，RNA，氨基酸...）进行归类的时候，我们使用字典序作为有效的字符串组织形式。

## Counting Subsets

### 背景知识

**集合和子集**: 在数学中，集合指一些对象的集合，这些对象又称为元素。如{sun, moon, star}。R指全体实数集合。空集，用{}表示，指没有任何元素的
集合。两个集合如果包含的元素完全一样，称两个集合相等。集合中的元素没有顺序，元素不能重复。如果集合A中所有元素都同时也是集合B中的元素，称集合A是
集合B的子集。如{sun, moon}是{sun, moon, star}的子集。空集是所有集合的子集。

### 问题

给定：一个正整数n(n<=1000)

输出：集合{1,2...n}的所有子集数，结果对1000000取余。

###  解决

这个问题的核心是效率。itertools.combinations的效率很低，因此需要直接计算排列组合公式。

    def solution():
        n = 847
        if n ==1:
            print(1)
        else:
            num = 1
            for i in range(n):
                comb = math.comb(n, i+1)
                num += comb
            print(num%1000000)
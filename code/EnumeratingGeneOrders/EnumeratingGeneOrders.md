## Enumerating Gene Orders

### 背景知识

#### 排列组合

排列组合是组合学最基本的概念。所谓排列，就是指从给定个数的元素中取出指定个数的元素进行排序。组合则是指从给定个数的元素中仅仅取出指定个数的元素，不考虑排序。

### 问题

给定：一个正整数n

输出：从1-n的n个正整数有多少种组合方式，并把各个方式列出来

### 解决

简单的组合问题求解。多少种组合方式就是n的阶乘。第一个位置有n种可能，第二位置有n-1种可能....直到最后一个位置只有一种可能。然后用python的itertools.permutations或者自己写for循环都可以列出所有可能性。

    def solution():
        n = 7
        iobjlist = list(itertools.permutations([str(i) for i in range(1,n+1)]))
        fout = open('result','w')
        fout.write(str(len(iobjlist))+'\n')
        for ex in iobjlist:
            fout.write(' '.join(ex))
            fout.write('\n')
        fout.close()

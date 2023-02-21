## [Enumerating Gene Orders](http://rosalind.info/problems/perm/)

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

### 扩展

点突变可以产生群体中的变异个体，但是不会产生一个新的物种。基因组重组可以产生重大的基因组变异。大部分会引起致命性的变异或严重的细胞损伤。正因为重组很少发生
在进化中，两个相近的物种，会有相似的基因组。为了比较这两个相似的基因组，一般研究人员会先将DNA划分为多个区段。两个相似基因组会包含多个
同义基因块（synteny blocks）。因此这个问题将这些区段用正整数代表，两个相似的基因组仅仅是正整数的顺序不同。

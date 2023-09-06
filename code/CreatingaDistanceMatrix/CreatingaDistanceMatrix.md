## [Creating a Distance Matrix](https://rosalind.info/problems/pdst/)

### 背景知识

**遗传距离(p-distance)**: 对于两个等长的DNA序列字符串，两者的遗传距离指两个字符串按位置不同的序列长度除以序列的长度。对于
一组序列，可以计算距离矩阵(distance matrix, D)。其中Di,j=d(si,sj)

### 问题

给定：以fasta格式提供的n个DNA序列(n<=10)

输出：计算距离矩阵

### 解决

这个问题相对简单，只需要两重循环计算每两个序列的距离即可，因为n数量也不大，没有做d(i,j)和d(j,i)的缓存。
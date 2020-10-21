## Finding a Shared Motif

### 背景知识

**公共子串**: 两个字符串包含的相同的子字符串。

### 问题

给定：一个fasta文件，包含k个DNA序列(k<=100)，每个序列长度不大于1kbp

输出：所有序列的最大公共子串

###  解决

核心问题是如何高效拿到两个字符串的公共子串，之后只需要循环就可以了。

寻找两个字符串的公共子串的方法参考[LONGEST COMMON SUBSTRING ALGORITHM](https://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php)的方法。


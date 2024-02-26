## [Motzkin Numbers and RNA Secondary Structures](https://rosalind.info/problems/motz/)

### 背景知识

**默慈金数**：一个给定的数的默慈金数是在一个圆上的个点间，画出彼此不相交弦的全部方法的总数。比如为5时，方法数为21，如下图:

<a href="https://rosalind.info/media/problems/motz/Motzkin_numbers.png" target="_blank"><img src="https://rosalind.info/media/problems/motz/Motzkin_numbers.png" /></a>

默慈金数的计算可以通过迭代完成。m0=m1=1，计算m(n)的时候，假设有n个点编号1-n，从点1开始，如果点1没有构成匹配(matching)，则后面有
m(n-1)种方式使后面的n-1个点形成匹配；如果点1构成了匹配，假设和点k构成了匹配，则一侧有k-2个点，另一侧有n-k个点，因此两侧分别有
m(k-2)和m(n-k)种方式形成匹配，这样就得到了递归公式:

<a href="https://latex.codecogs.com/png.image?\dpi{110}&space;m_{n}=m_{n-1}&plus;\sum_{k=2}^{n}m_{k-2}\ast&space;m_{n-k}" target="_blank"><img src="https://latex.codecogs.com/png.image?\dpi{110}&space;m_{n}=m_{n-1}&plus;\sum_{k=2}^{n}m_{k-2}\ast&space;m_{n-k}" /></a>

### 问题

给定：给定一个RNA序列s长度约300bp

输出：序列s所有不交叉匹配情况的数目，结果对1000000取模。

### 解决

递归部分由一下函数定义，和上图区别在引入*motzkin_memo*记录已经计算的*motzkin numbers*，且限制只能AU，CG才能成边。

    def _get_motzkin_numbers(s, n, motzkin_memo):
        if n <= 1:
            return 1
        if motzkin_memo.get((s, n),0):
            return motzkin_memo[(s, n)]
        Cn = _get_motzkin_numbers(s[1:], n-1, motzkin_memo)
    
        for k in range(1, n):
            if (s[0], s[k]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]:
                Cn += _get_motzkin_numbers(s[1:k], k-1, motzkin_memo) * _get_motzkin_numbers(s[k+1:], n-k-1, motzkin_memo)
        # Memorize calculated Motzkin Numbers values
        motzkin_memo[(s, n)] = Cn
        return Cn

调用部分：

    seq_name, seq_string = [], []
    with open ("rosalind_motz.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    s = seq_string[0]
    print(s)
    nodes = len(s)
    motzkin_memo = {} #  Memorize calculated Motzkin Numbers values
    motzkin_number= _get_motzkin_numbers(s, nodes, motzkin_memo)
    print("catalan number: {}".format(motzkin_number))
    print("modulo 1,000,000: {}".format(motzkin_number%1000000))

### 扩展

在[Catalan Numbers and RNA Secondary Structures](https://rosalind.info/problems/cat/)中讨论了偶数点的情况，默慈金数则可以
用于奇数点的情况。
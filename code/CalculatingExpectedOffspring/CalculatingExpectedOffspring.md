## Calculating Expected Offspring (计算子代期望)

### 背景知识

#### 期望

数学期望是试验中每次可能结果的概率乘以其结果的总和，是最基本的数学特征之一。它反映随机变量平均取值的大小。

严格的数学定义： 设离散型随机变量X的分布律为

<img src="https://latex.codecogs.com/gif.latex?P\left&space;\{&space;X=x_{k}&space;\right&space;\}=&space;p_{k},k=1,2,\cdots" title="P\left \{ X=x_{k} \right \}= p_{k},k=1,2,\cdots" />

若级数

<img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{\infty&space;}x_{k}p_{k}" title="\sum_{k=1}^{\infty }x_{k}p_{k}" />

绝对收敛，则称级数<img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{\infty&space;}x_{k}p_{k}" title="\sum_{k=1}^{\infty }x_{k}p_{k}" />的和为随机变量X的数学期望，记为E(X), 即

<img src="https://latex.codecogs.com/gif.latex?E(X)=\sum_{k=1}^{\infty&space;}x_{k}p_{k}" title="E(X)=\sum_{k=1}^{\infty }x_{k}p_{k}" />

设连续型随机变量X的概率密度为f(x), 若积分

<img src="https://latex.codecogs.com/gif.latex?\int_{-\infty&space;}^{\infty&space;}xf(x)dx" title="\int_{-\infty }^{\infty }xf(x)dx" />

绝对收敛，则积分<img src="https://latex.codecogs.com/gif.latex?\int_{-\infty&space;}^{\infty&space;}xf(x)dx" title="\int_{-\infty }^{\infty }xf(x)dx" />的值为随机变量X的数学期望，记为E(X), 即

<img src="https://latex.codecogs.com/gif.latex?E(X)=\int_{-\infty&space;}^{\infty&space;}xf(x)dx" title="E(X)=\int_{-\infty }^{\infty }xf(x)dx" />


#### 均匀分布

均匀分布的分布函数为

<img src="https://latex.codecogs.com/gif.latex?F(X)=\left\{\begin{matrix}&space;0,x<a\\&space;\frac{x-a}{b-a},a<x<b\\&space;1,x>b\\&space;\end{matrix}\right." title="F(X)=\left\{\begin{matrix} 0,x<a\\ \frac{x-a}{b-a},a<x<b\\ 1,x>b\\ \end{matrix}\right." />

对于离散型随机变量，设X~U(a,b), 其概率密度为

<img src="https://latex.codecogs.com/gif.latex?f(x)=\left\{\begin{matrix}&space;\frac{1}{b-a},a<x<b\\&space;0,other\\&space;\end{matrix}\right." title="f(x)=\left\{\begin{matrix} \frac{1}{b-a},a<x<b\\ 0,other\\ \end{matrix}\right." />

掷骰子就是一个均匀分布的例子，假设扔一个六面的骰子，平均每个出现的点数的期望是3.5(虽然不可能掷出3.5)。计算公式为

<img src="https://latex.codecogs.com/gif.latex?E(X)&space;=&space;\sum_{k=1}^{6}k\times&space;Pr(X=k)=3.5" title="E(X) = \sum_{k=1}^{6}k\times Pr(X=k)=3.5" />

### 问题

输入为6个非负整数，每个都不超过20000，每个整数代表了一个群体中的一种父代类型，每种类型包含父亲和母亲的基因型组合。每个序号基因性
组合如下：

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

需要求出：显性子代的期望数目，假设每种父代组合产生两个子代。

### 解决

这不是一个编程算法题，而是一个概率问题，只需要按照期望公式求解，即算出每个父代基因型组合的子代数目乘以子代是显性的概率。
子代数目已经固定给出是2，每个父代组合的显性子代概率计算过程如下。

1.AA-AA

|  | A | A |
| ------------- | ------------- | ------------- |
| A  | AA  | AA |
| A  | AA  | AA |

p1 = 1

2.AA-Aa

|  | A | A |
| ------------- | ------------- | ------------- |
| A  | AA  | AA |
| a  | Aa  | Aa |

p2 = 1

3.AA-aa

|  | A | A |
| ------------- | ------------- | ------------- |
| a | Aa  | Aa |
| a  | Aa  | Aa |

p3 = 1

4.Aa-Aa

|  | A | a |
| ------------- | ------------- | ------------- |
| A | AA  | Aa |
| a  | Aa  | aa |

p4 = 0.75

5.Aa-aa

|  | A | a |
| ------------- | ------------- | ------------- |
| a | Aa  | aa |
| a  | Aa  | aa |

p5 = 0.5

6.aa-aa

|  | a | a |
| ------------- | ------------- | ------------- |
| a | aa  | aa |
| a  | aa  | aa |

p6 = 0

因此，计算结果为(p1\*n1+p2\*n2+p3\*n3+p4\*n4+p5\*n5)*2, 其中n1-n5为前5个整数。

    def main():
        s = '19649 18991 17249 18533 19874 16390'
        a1,a2,a3,a4,a5,a6 = [int(i) for i in s.split(' ')]
    
        print((a1+a2+a3+0.75*a4+0.5*a5)*2)
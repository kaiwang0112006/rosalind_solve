## Calculating Expected Offspring (计算子代期望)

### 背景知识

#### 期望

数学期望是试验中每次可能结果的概率乘以其结果的总和，是最基本的数学特征之一。它反映随机变量平均取值的大小。

严格的数学定义： 设离散型随机变量X的分布律为

<img src="http://www.sciweavers.org/tex2img.php?eq=P%20%5Cbig%5C%7BX%3Dx_%7Bk%7D%20%5Cbig%5C%7D%20%3Dp_%7Bk%7D%20%2C%20k%3D1%2C2%2C%20%5Ccdots%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="P \big\{X=x_{k} \big\} =p_{k} , k=1,2, \cdots " width="222" height="21" />

若级数

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Csum_%7Bk%3D1%7D%5E%7B%20%5Cinfty%20%7D%20%20x_%7Bk%7D%20%20p_%7Bk%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\sum_{k=1}^{ \infty }  x_{k}  p_{k} " width="71" height="50" />

绝对收敛，则称级数<img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{\infty&space;}x_{k}p_{k}" title="\sum_{k=1}^{\infty }x_{k}p_{k}" />的和为随机变量X的数学期望，记为E(X), 即

<img src="http://www.sciweavers.org/tex2img.php?eq=E%20%5Cbig%28X%5Cbig%29%20%3D%20%5Csum_%7Bk%3D1%7D%5E%7B%20%5Cinfty%20%7D%20x_%7Bk%7Dp_%7Bk%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="E \big(X\big) = \sum_{k=1}^{ \infty } x_{k}p_{k}" width="132" height="50" />

设连续型随机变量X的概率密度为f(x), 若积分

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cint_%7B%20-%5Cinfty%20%7D%5E%7B%20%5Cinfty%20%7D%20xf%28x%29%20%5C%2C%20dx&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\int_{ -\infty }^{ \infty } xf(x) \, dx" width="108" height="49" />

绝对收敛，则积分<img src="https://latex.codecogs.com/gif.latex?\int_{-\infty&space;}^{\infty&space;}xf(x)dx" title="\int_{-\infty }^{\infty }xf(x)dx" />的值为随机变量X的数学期望，记为E(X), 即

<img src="http://www.sciweavers.org/tex2img.php?eq=E%28X%29%20%3D%20%5Cint_%7B%20-%5Cinfty%20%7D%5E%7B%20%5Cinfty%20%7D%20xf%28x%29%20%5C%2C%20dx&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="E(X) = \int_{ -\infty }^{ \infty } xf(x) \, dx" width="167" height="49" />





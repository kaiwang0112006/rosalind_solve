## [Inferring Protein from Spectrum](https://rosalind.info/problems/spec/)

### 背景知识

加权字符串的前缀谱是其所有前缀权重的集合。

### 问题

给定：给定一个长度为n的正实数数组L

输出：以给定作为蛋白质光谱推断蛋白质序列（长度为L-1）

示例输入: 

    3524.8542
    3710.9335
    3841.974
    3970.0326
    4057.0646

示例出: 

    WMQS

###  解决

首先通过数组元素后项减前项得到序列的质量，再查[单同位素质量表](https://rosalind.info/glossary/monoisotopic-mass-table/)。
只有一点需要注意：保留相同的小数点位数，否则可能查不到序列。

    with open('rosalind_spec.txt','r') as f:
        L = []
        for eachline in f:
            L.append(float(eachline.strip()))

    mass_table = {'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,'G':57.02146,'H':137.05891,'I':113.08406,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333}

    aa_masses = []
    for i in range(len(L) - 1):
        aa_mass = round(L[i + 1] - L[i], 4)
        aa_masses.append(aa_mass)

    rnd_mass_table = {}
    for k, v in mass_table.items():
        rnd_mass_table[round(v, 4)] = k

    prot = ''
    for aa in aa_masses:
        prot += rnd_mass_table[aa]

    print(prot)

### 扩展

在["Calculating Protein Mass"](https://kaiwang0112006.github.io/rosalind_solve/code/CalculatingProteinMass/CalculatingProteinMass)
一文中，我们简要提到了一种名为质谱法的化学分析方法，其目的是测量粒子或分子的质量电荷比。 在质谱仪中，样品被蒸发（变成气体），
然后样品中的粒子被电离。 产生的离子被置于电磁场中，电磁场会根据离子的电荷和质量将其分离。 质谱仪的输出是质谱，或者说是离子可能的质量-电荷比值与具有
这些质量-电荷比值的离子的强度（实际观察到的频率）之间的关系图。

目前，暂且忽略电荷，将离子的单异位质量列表视为简化的光谱。 研究人员不具备逐个氨基酸检查蛋白质的廉价技术（分子过于微小）。 相反，为了确定蛋白质的结构，
会将几份蛋白质分割成更小的片段，然后称量所得片段的重量。 为此，假设每个切口（断裂点）都发生在两个氨基酸之间，并且可以测量所有可能切口所产生碎片的质量。

例如，"PRTEIN"（未知）蛋白质可以有五种切割方式: "P"和 "RTEIN"；"PR "和 "TEIN"；"PRT "和 "EIN"；"PRTE "和 "IN"；"PRTEI "和 "N"。 
然后，我们就可以测量所有片段（包括整个字符串）的质量。 蛋白质的 "左 "端称为 N 端，与蛋白质串前缀（P、PR、PRT、PRTE、PRTEI）相对应的离子称为 b 离子。 
蛋白质的 "右 "端称为 C 端，与蛋白质串后缀（N、IN、EIN、TEIN、RTEIN）相对应的离子称为 y 离子。 相邻两个 b 离子（或 y 离子）的质量之差就是一个
氨基酸残基的质量；例如，"PRT "和 "PR "的质量之差就是 "T "的质量。 推而广之，知道了蛋白质中每个 b 离子的质量，我们就能推断出蛋白质的特性。
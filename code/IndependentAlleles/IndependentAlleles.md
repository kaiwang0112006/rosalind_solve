## Independent Alleles

### 背景知识

**独立事件**: 概率论的基本概念之一.两个事件A与B，若事件B发生与否同事件A发生的概率无关，反之亦然，则称A与B是相互独立的事件.两个事件A与B相互独立的充分必要条件是P(AB)=P(A)P(B)

**孟德尔第二定律**：自由组合规律(law of independent assortment)是现代生物遗传学三大基本定律之一。当具有两对（或更多对）相对性状的亲本进行杂交，在子一代产生配子时，在等位基因分离的同时，非同源染色体上的非等位基因表现为自由组合。

### 问题

给定：两个正整数k和N，其中k<=7,N<=2<sup>k</sup>(2的k次方)，假设第0代的基因型是AaBb，每代产生两个子代（所以N<=2<sup>k</sup>），每个子代总是和AaBb交配

输出：第k代至少有N个子代是AaBb的概率。（基于孟德尔第二定律）

### 解决

第一步找到在第k代每个子代是AaBb的概率p，第二步就可以假设在第k代的2<sup>k</sup>个个体中有i个个体是AaBb的概率（i=N,N+1,...2<sup>k</sup>）,加和即是结果。

##### 单个子代的p值计算

关于第一步，首先用了一种麻烦的方法，即模拟计算每代的子代各基因型的概率，但计算完成后发现每代的各个概率其实是一样的，应该是因为每一代的各个基因型概率都是独立事件，模拟的结果只是将全概率公式展开计算，和直接计算一代的结果是一样的。

    def Mendel(S,T):
        '''
        输入父亲和母亲的基因型，如S='AaBb',
        T='AAbb',得到子代各个基因型的概率：
        {'AABb': 0.25, 'AAbb': 0.25, 'AaBb': 0.25, 'Aabb': 0.25}
        '''
        sub1 = getsubtype(S)
        sub2 = getsubtype(T)
        comb = []
        #print(S,sub1,T,sub2)
        for i in sub1:
            for j in sub2:
                comb.append(min(i[0],j[0])+max(i[0],j[0])+min(i[1],j[1])+max(i[1],j[1]))
        cb = dict(collections.Counter(comb))
        sumv = sum(cb.values())
        for k in cb:
            cb[k] = cb[k]/sumv
        return cb

    def calAa(k):
        '''
        迭代调用得到第k代的子代各个基因型的概率
        '''
        if k==0:
            return Mendel("AaBb","AaBb")
        else:
            pdict = calAa(k-1)
            gentypes = list(pdict.keys())
            rlist = {}
            for t in pdict:
                rdict = Mendel(t,"AaBb")
                #print(t,"AaBb",rdict)
                rlist[(t,"AaBb")] = rdict
                gentypes = gentypes+list(rdict.keys())
            returnrtpes = {}
            for t in set(gentypes):
                returnrtpes[t] = 0
                for g in pdict:
                    returnrtpes[t] += pdict[g]*rlist[(g,"AaBb")].get(t,0)
            print(k, returnrtpes) # 这里输出了每代的概率分布
            return returnrtpes

    calAa(4)
    '''
    1 generation, genotype distribution {'AAbb': 0.0625, 'aabb': 0.0625, 'AaBB': 0.125, 'Aabb': 0.125, 'AABb': 0.125, 'AaBb': 0.25, 'aaBb': 0.125, 'aaBB': 0.0625, 'AABB': 0.0625}
    2 generation, genotype distribution {'AAbb': 0.0625, 'aabb': 0.0625, 'AaBB': 0.125, 'Aabb': 0.125, 'AABb': 0.125, 'AaBb': 0.25, 'aaBb': 0.125, 'aaBB': 0.0625, 'AABB': 0.0625}
    3 generation, genotype distribution {'AAbb': 0.0625, 'aabb': 0.0625, 'AaBB': 0.125, 'Aabb': 0.125, 'AABb': 0.125, 'AaBb': 0.25, 'aaBb': 0.125, 'aaBB': 0.0625, 'AABB': 0.0625}
    4 generation, genotype distribution {'AAbb': 0.0625, 'aabb': 0.0625, 'AaBB': 0.125, 'Aabb': 0.125, 'AABb': 0.125, 'AaBb': 0.25, 'aaBb': 0.125, 'aaBB': 0.0625, 'AABB': 0.0625}
    '''

因此，可以直接用孟德尔第二定律得到：

  | | AB |	Ab	| aB	| ab |
  |  ----  | ----  | ----  | ----  | ----  |
  | **AB** | AABB | AABb | AaBb | AaBb |
  | **Ab** | AABb | AAbb | AaBb | Aabb |
  | **aB** | AaBB | AaBb | aaBB | aaBb |
  | **ab** | AabB | Aabb | aaBb | aabb |

**第一步的结果为** p = 0.25

##### k代中N个目标基因型概率计算

第二步这里使用了二项分布，要计算2<sup>k</sup>个个体中有i个基因型为AaBb（i=N,N+1,...2<sup>k</sup>），即做了2<sup>k</sup>个伯努利实验，每个实验是AaBb的概率是p，不是的概率是1-p，且p不等于1-p，即不能用古典概型简化。因此概率公式为

<a href="https://www.codecogs.com/eqnedit.php?latex=C_{2^{k}}^{i}p^{i}(1-p)^{2^{k}-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C_{2^{k}}^{i}p^{i}(1-p)^{2^{k}-1}" title="C_{2^{k}}^{i}p^{i}(1-p)^{2^{k}-1}" /></a>

代码部分：

    pr = 0
    for n in range(N,(2**k)+1):
        up = len(list(combinations(list(range(2**k)), n)))
        pr += up*(pdict['AaBb']**n)*((1-pdict['AaBb'])**(2**k-n))

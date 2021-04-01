## [Genome Assembly as Shortest Superstring](http://rosalind.info/problems/long/)

### 背景知识

**字符串超集**: 对于一个字符串集合，一个包含集合中所有子字符串的大字符串称为超字符串

### 问题

给定：给定一个fasta文件包含一系列字符串

输出：最短超字符串包含fasta文件中所有字符串，假设fasta中的序列可以首尾连接。

### 解决

这是一个基因组组装的简化版问题，首先定义一个函数可以返回两个字符串头部（或者尾部）的overlap

    def findoverlap(s1,s2,reverse_op=False):
        '''
        parms: s1=ATTAGACCTG, s2=CCTGCCGGAA
        reverse_op=False 时返回 CCTG
        reverse_op=True 时返回 A
        '''

        if reverse_op:
            s1, s2 = s2, s1

        l = min(len(s1),len(s2))
        while s1[-1*l:] != s2[:l]:
            #print('findoverlap', l, s1[-1*l:],s2[:l])
            l -=1
            if l==0:
                break
        if l == 0:
            return ''
        else:
            return s1[-1*l:]

之后就可以通过循环fasta中的序列，找到overlap最大的另一个序列进行合并

    def glue(sl):
        maxl = 0
        overlap = ''
        org = ''
        ind = None
        st = sl[0]
        for i in range(1,len(sl)):
            overlap1 = findoverlap(st,sl[i],reverse_op=False)
            overlap2 = findoverlap(st,sl[i],reverse_op=True)

            if len(overlap1)>len(overlap2) and len(overlap1)>maxl:
                maxl = len(overlap1)
                overlap = overlap1
                org = False
                ind = i
            elif len(overlap2)>=len(overlap1) and len(overlap2)>maxl:
                maxl = len(overlap2)
                overlap = overlap2
                org = True
                ind = i
            #print(st, sl[i], overlap1, overlap2,org)

        if org == True:
            comb = sl[ind] + st.replace(overlap,'')
        elif org == False:
            comb = st + sl[ind].replace(overlap,'')
        sed = sl[ind]
        sl = [i for i in sl if i not in [st, sed]]

        return [comb] + sl

  

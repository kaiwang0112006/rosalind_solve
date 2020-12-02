## Finding a Protein Motif

### 背景知识

#### motif 

sequence motifs可以被定义为一段特定的蛋白质（蛋白质序列）。一个简单的motif可以是一个模式pattern，而这个模式被这个group中的所有成员共享。例如 N{P}[ST]{P}（N-glycosylation motif）。当然也有更复杂的motif模型。Motif有时和特定的功能联系一起。

motif的常见格式见：https://prosite.expasy.org/scanprosite/scanprosite_doc.html#mo_motifs

#### uniprot

UniProt 是 Universal Protein 的英文缩写，是信息最丰富、资源最广的蛋白质数据库

uniprot_id即蛋白质在该数据库中的id，页面可以通过 *http://www.uniprot.org/uniprot/uniprot_id* 进行浏览，
fasta格式的蛋白质序列通过 *http://www.uniprot.org/uniprot/uniprot_id.fasta* 获取。

### 问题

给定最多15个蛋白质的uniprot_id，返回包含N-glycosylation motif的uniprot_id和找到的motif的所有起始位置

### 解决

这其实就是一个用正则表达式做字符串搜索的任务。关键函数为输入蛋白质序列和需要搜索的motif pattern，返回搜索到的起始位置。

    def getRE_result(seqs, query):
        '''
        :param seqs: protein seqence.
        :param query: search pattern in regular expression.
        :return: list that contain all start position.
        '''
    
        ms = [str(m.start() + 1) for m in re.finditer(query, seqs)]
        return ms
        
一个核心问题是motif pattern的定义，直接用 r'N[^P]\(S|T)[\^P]' 无法应对搜索结构有overlap的情况，应该为 r'(?=(N[^P]\(S|T)[\^P]))'

接下来只需要循环15个uniprot_id获取蛋白序列即可。

    def solution():
        inputstr = '''
    P20268
    Q5WFN0
    P02974_FMM1_NEIGO
    P22457_FA7_BOVIN
    P01189_COLI_HUMAN
    P19823_ITH2_HUMAN
    P07359_GPBA_HUMAN
    P36913_EBA3_FLAME
    Q4FZD7
    P05783_K1CR_HUMAN
    P21810_PGS1_HUMAN
    B8GYE3
    Q8WW18
        '''
        query = r'(?=(N[^P](S|T)[^P]))'
        inputlist = inputstr.split()
        baseUrl = "http://www.uniprot.org/uniprot/"
        for i in range(len(inputlist)):
            cID = inputlist[i]
            currentUrl = baseUrl + cID + ".fasta"
            response = requests.post(currentUrl)
            cData = ''.join(response.text)
            Seq = StringIO(cData)
            pSeq = SeqIO.to_dict(SeqIO.parse(Seq, 'fasta'))
            msall = []
            for k in pSeq:
                seqs = str(pSeq[k].seq)
                ms = getRE_result(seqs, query)
                msall = msall+ms
            if len(msall)>0:
                print(cID)
                print(' '.join(msall))
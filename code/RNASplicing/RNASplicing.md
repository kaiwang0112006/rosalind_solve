## RNA Splicing

### 背景知识

1.外显子和内含子

### 问题

给定：一个fasta文件，其中第一个序列为1kbp左右的DNA序列，其他序列为内含子

输出：去除内含子后返回外显子翻译得到的蛋白质序列

###  解决

第一步识别和去除内含子，第二步翻译即可。

    def main():
        with open("example.fasta") as handle:
            count = 0
            for record in SeqIO.parse(handle, "fasta"):
                if count==0:
                    mainseq = str(record.seq)
                else:
                    mainseq = mainseq.replace(str(record.seq), ' ')
                count+=1
        exons = mainseq.split(' ')

        result = ''
        for e in exons:
            result+=Seq(e).translate()
        print(result)

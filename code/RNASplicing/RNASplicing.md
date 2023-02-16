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

### 扩展

从DNA转录得到RNA并不是简单的T->U的碱基替换。在细胞内，首先通过RNA聚合酶切断DNA双链的互补碱基键，然后沿着其中一条模版链，添加核苷酸并催化反应是相邻核苷酸聚合形成磷酸二酯键。这一步形成了前体mRNA，还需要在剪接体的作用下切割前体mRNA中的内含子部分序列，再将外显子连接起来称为真正的mRNA，称为RNA剪接（RNA splicing）。有趣的是剪接体也是RNA和蛋白质构成，因此RNA剪接和转录过程仍然存在“先有蛋还是先有鸡”的未解问题。

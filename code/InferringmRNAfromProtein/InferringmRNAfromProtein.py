# -*- coding:utf-8 -*-
from collections import defaultdict

def generate_codentable():
    RNA_Codons = {
        # 'M' - START, '_' - STOP
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UGU": "C", "UGC": "C",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "UUU": "F", "UUC": "F",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAU": "H", "CAC": "H",
        "AUA": "I", "AUU": "I", "AUC": "I",
        "AAA": "K", "AAG": "K",
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUG": "M",
        "AAU": "N", "AAC": "N",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UGG": "W",
        "UAU": "Y", "UAC": "Y",
        "UAA": "_", "UAG": "_", "UGA": "_"
    }
    proteincoden = defaultdict(list)

    for k in RNA_Codons:
        v = RNA_Codons[k]
        proteincoden[v].append(k)
    return proteincoden


def main():
    #print(dict(generate_codentable()))

    proteincoden = {'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'C': ['UGU', 'UGC'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'],
     'F': ['UUU', 'UUC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'H': ['CAU', 'CAC'], 'I': ['AUA', 'AUU', 'AUC'],
     'K': ['AAA', 'AAG'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'M': ['AUG'], 'N': ['AAU', 'AAC'],
     'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
     'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
     'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'W': ['UGG'], 'Y': ['UAU', 'UAC'], '_': ['UAA', 'UAG', 'UGA']}

    protein = "MIKPIIIAPLWWAYGDDIMSDIMYRKTNHSWIIMGMKAAGVCADHTCVCDAFVGQHHGFMVCCEFTLSASWAHKEMCRTMMTTASWAHPVPARAMSNWVAKPFWCTAKVARTLDLAVQPNKMKCDSEPCDRIVVNMCDAASIIGLFSCMEELIDDDMDIYERINASNFSFADQLYCTAPVRTWAPPFWYRTDSKFAKKCCQNCKKWWEAVWSDWDGDMYWRMSRTENTTWGGKEGDYCACTQFHENSNIPCPRMTDCISQSLWLHLAYCVKLKDMFYNGMMNMATSMCTQKSGQCFKIWCMIVAQLLFFRRAHCQLLVIMVLGQYKCECHCTVKFGGPSVGAQKRITPFNTEQKGWPNTRAPIKSEPYRSTFIPNHCAPYRAMKMDQYIFNEFWVTGRMYAFRVEPNCGPRCISIRDCYLNIHLNVEFTEFIWHDQRIGRGIMSRIYLGVFNTKTHYFNYLEVHSNTHDDCGVMFWDGIPVTAEADNDCGMCLGVYAMVKMNCNTCMYPFFDLMDPPWEGCTLFHKYEQVCCMCRYPRFPRTLNQALFLDNALPRCDNVKEGSGIQPCCEEDHLTLWRPLHWLKWNYVNMKKYRPFEYSSILPNPGGVWTQNYWVFCHKPEAFVFKCYYLMTDLDLTTPIGHVLWSRRRHTCIARAQSKDHHQTIELNAMKNSFWTMMPVKFHQDCITLPGVMWFDWWGNMVESAHAHIRVWLKKCAKCAPFMKTTIEGENAPCTVFRMLWHCWANFPWEMFPYYEYGPMGYGMCYDEWETFRYYDERTPTEHSTWITYSYSDECWSHDCIPIIPVTKYRFFSNFAIGRFQEGTTCRRCMVGFGTYQAAIDAWGSCLVGHPIRIPVFCEHFAYAWGGYWWWEFPDYRRMCRELAHHTAWHNQLCNDKRMWWVCMCLFYMYMNWEAWRLHMGKETFFSRHFNAWWVPERGPALTFRCTSPTGVHKNIAHSQVTCQRKFDMFHHKIKVEHGFIDCDMCVMQSWMRQGIIAIL"
    n = 1
    for aa in protein:
        n = n*len(proteincoden[aa])
    n = n*len(proteincoden['_'])
    print(n%1000000)

if __name__ == "__main__":
    main()
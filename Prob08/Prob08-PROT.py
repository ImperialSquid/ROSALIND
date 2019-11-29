with open("Prob08-PROT-in.txt", "r") as f:
    dnaString = f.readline().strip()

dnaProtDict = {"UUU":"F",    "CUU":"L", "AUU":"I", "GUU":"V",
"UUC":"F",    "CUC":"L", "AUC":"I", "GUC":"V",
"UUA":"L",    "CUA":"L", "AUA":"I", "GUA":"V",
"UUG":"L",    "CUG":"L", "AUG":"M", "GUG":"V",
"UCU":"S",    "CCU":"P", "ACU":"T", "GCU":"A",
"UCC":"S",    "CCC":"P", "ACC":"T", "GCC":"A",
"UCA":"S",    "CCA":"P", "ACA":"T", "GCA":"A",
"UCG":"S",    "CCG":"P", "ACG":"T", "GCG":"A",
"UAU":"Y",    "CAU":"H", "AAU":"N", "GAU":"D",
"UAC":"Y",    "CAC":"H", "AAC":"N", "GAC":"D",
"UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
"UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
"UGU":"C",    "CGU":"R", "AGU":"S", "GGU":"G",
"UGC":"C",    "CGC":"R", "AGC":"S", "GGC":"G",
"UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
"UGG":"W",    "CGG":"R", "AGG":"R", "GGG":"G"}

codons = [dnaString[i:i+3] for i in range(0,len(dnaString),3)]
prots = [dnaProtDict[codon] for codon in codons]
protString = "".join(prots)
protString = protString.replace("Stop", "")

with open("Prob08-PROT-out.txt", "w") as f:
    f.write(protString)

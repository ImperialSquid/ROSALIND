seqs = dict()

def getCGContent(seq):
    return (seq.count("C")+seq.count("G"))/len(seq)

with open("Prob05-GC-in.txt", "r") as f:
    currentSeq = ""
    for line in f:
        if line[0] == ">":
            currentSeq = line.strip()[1:]
            seqs[currentSeq] = ""
        else:
            seqs[currentSeq] = seqs.get(currentSeq) + line.strip()

highestCGContent = 0
highestCGid = ""
for key in seqs.keys():
    if getCGContent(seqs[key]) > highestCGContent:
        highestCGContent = getCGContent(seqs[key])
        highestCGid = key

with open("Prob05-GC-out.txt", "w") as f:
    f.write(highestCGid)
    f.write("\n")
    f.write(str(highestCGContent*100))

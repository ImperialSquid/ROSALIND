with open("Prob1-DNA-in.txt", "r") as f:
    bases = f.readline()

baseCounts = [str(bases.count(x)) for x in list("ACGT")]

with open("Prob1-DNA-out.txt", "w") as f:
    f.write(" ".join(baseCounts))

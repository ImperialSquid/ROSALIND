from itertools import zip_longest

dnaStrings = []
with open("Prob11-CONS-in.txt", "r") as f:
    for line in f.readlines():
        if line[0] == ">":
            dnaStrings.append("")
        else:
            dnaStrings[len(dnaStrings)-1] = dnaStrings[len(dnaStrings)-1] + line.strip()

pos = []  # represents each position in the string
baseCounts = {"A":[], "C":[], "G":[], "T":[]}
for eles in zip_longest(*dnaStrings):
    pos.append(eles)  # basically flips the matrix along the diagonal
    for base in baseCounts.keys():
        baseCounts[base].append(len([ele for ele in eles if ele == base]))

cons = ""
for i in range(len(dnaStrings[0])):  # problem def guarantees atrings are the same length
    most = -1
    lett = ""
    for base in "ACGT":
        if baseCounts[base][i] > most:
            most = baseCounts[base][i]
            lett = base
    cons += lett

print(cons)
for base in "ACGT":
    print(base+": "+" ".join([str(x) for x in baseCounts[base]]))

with open("Prob11-CONS-out.txt", "w") as f:
    f.write(cons+"\n")
    for base in "ACGT":
        f.write(base + ": " + " ".join([str(x) for x in baseCounts[base]]) +"\n")

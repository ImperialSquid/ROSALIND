with open("Prob03-REVC-in.txt", "r") as f:
    bases = f.readline()

bases = bases[::-1]

for i, nt in enumerate(list("ACGT")):
    bases = bases.replace(nt, str(i))

for i, cnt in enumerate(list("TGCA")):
    bases = bases.replace(str(i), cnt)

with open("Prob03-REVC-out.txt", "w") as f:
    f.write(bases)

with open("Prob02-RNA-in.txt", "r") as f:
    bases = f.readline()

bases = bases.replace("T", "U")

with open("Prob02-RNA-out.txt", "w") as f:
    f.write(bases)

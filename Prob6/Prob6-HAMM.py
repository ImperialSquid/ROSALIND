with open("Prob6-HAMM-in.txt", "r") as f:
    seq1 = f.readline()
    seq2 = f.readline()

hammingDist = 0
for s1, s2 in zip(seq1, seq2):
    if s1 != s2:
        hammingDist += 1

with open("Prob6-HAMM-out.txt", "w") as f:
    f.write(str(hammingDist))

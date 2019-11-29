with open("Prob9-SUBS-in.txt", "r") as f:
    superstr = f.readline().strip()
    substr = f.readline().strip()

indexes = []
index = -1  # set to -1 to negate the +1 on first search
while True:
    index = superstr.find(substr, index + 1)  # start from index+1 else python will find the same result infinitely
    if index == -1:
        break
    else:
        indexes.append(index)

with open("Prob9-SUBS-out.txt", "w") as f:
    f.write(" ".join([str(x + 1) for x in indexes]))

with open("Prob10-FIBD-in.txt", "r") as f:
    line = f.readline().strip()
    iters = int(line.split(" ")[0])
    maxAge = int(line.split(" ")[1])

# each element represents the number of rabbits of the age of the respective index
currGen = [0]*maxAge
currGen[0] = 1
nextGen = [0]*maxAge

for iter in range(iters-1):
    nextGen = [sum(currGen[1:])] + currGen[:-1]
    # every mature rabbit after index 0 is mature so they get summed for the new births, rest of the elements are shifted up one
    currGen = nextGen

with open("Prob10-FIBD-out.txt", "w") as f:
    f.write(str(sum(currGen)))
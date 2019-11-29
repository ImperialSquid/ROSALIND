with open("Prob07-IPRB-in.txt", "r") as f:
    ints = [int(x) for x in f.readline().split(" ")]
    k = ints[0]
    m = ints[1]
    n = ints[2]

t = k + m + n
prob = k/t + (m*k + n*k + n*m +3*m*(m-1)/4)/(t*(t-1))
print(prob)

with open("Prob07-IPRB-out.txt", "w") as f:
    f.write(str(prob))

with open("Prob4-FIB-in.txt", "r") as f:
    in_ = f.readline()
    gens = int(in_.split(" ")[0])
    offspring = int(in_.split(" ")[1])

adult = 0
adultPrev = 0
chld = 0
chldPrev = 1
for gen in range(gens-1):
    adult = adultPrev + chldPrev
    chld = adultPrev * offspring

    adultPrev = adult
    chldPrev = chld

with open("Prob4-FIB-out.txt", "w") as f:
    f.write(str(adult+chld))

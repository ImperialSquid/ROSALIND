import os

probCode = "GC"
probNum = "5"

try:
    os.mkdir("Prob{}".format(probNum))
except:
    pass

with open("Prob{0}\/Prob{0}-{1}.py".format(probNum, probCode), "w") as f:
    f.write("with open(\"Prob{}-{}-in.txt\", \"r\") as f:\n".format(probNum,probCode))
    f.write("    pass\n")
    f.write("\n")
    f.write("pass\n")
    f.write("\n")
    f.write("with open(\"Prob{}-{}-out.txt\", \"w\") as f:\n".format(probNum, probCode))
    f.write("    pass\n")

with open("Prob{0}\/Prob{0}-{1}-in.txt".format(probNum,probCode), "w") as f:
    f.write("")

with open("Prob{0}\/Prob{0}-{1}-out.txt".format(probNum,probCode), "w") as f:
    f.write("")

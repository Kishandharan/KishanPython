f1 = open("in2.txt", "r")
f2 = open("out1.txt", "w")
line = f1.readline()
tables1 = line.split(",")
tables2 = []
output = ""

for line in tables1:
    temp = int( line.replace("\n", "") )
    tables2.append(temp)

for j in tables2:
    for i in range(1, 11, 1):
        output += str(i) + " x " + str(j) + " = " + str(i*j) + "\n"
    output += "\n"

f2.write(output)

f1.close()
f2.close()

f1 = open("in2.txt", "r")
line = f1.readline()
tables1 = line.split(",")
tables2 = []

for line in tables1:
    temp = int( line.replace("\n", "") )
    tables2.append(temp)

for j in tables2:
    for i in range(1, 11, 1):
        print(i, "x", j, "=", i*j)
    print("")

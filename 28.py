f1 = open("in1.txt", "r")
lines = []

for line in f1:
    temp = int( line.replace("\n", "") )
    lines.append(temp)

for j in lines:
    for i in range(1, 11, 1):
        print(i, "x", j, "=", i*j)
    print("")


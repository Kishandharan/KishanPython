start1 = int(input("Start1: "))
end1 = int(input("End1: "))
start2 = int(input("Start1: "))
end2 = int(input("End2: "))
fname = input("FileName: ")

f1 = open(fname, "w")

for t in range(start1, end1+1):
    for n in range(start2, end2+1):
        f1.write(f"{n} * {t} = {n*t}")
    f1.write("\n")

f1.close()

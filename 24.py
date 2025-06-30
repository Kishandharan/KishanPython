num1 = int(input("Start: "))
num2 = int(input("End: "))

tstart = 3
tend = 10

for j in range(tstart, tend+1, 1):
    for i in range(num1, num2+1, 1):
        print(f"{i}x{j}={i*j}")
    print()




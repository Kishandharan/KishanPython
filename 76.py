countries = []
capitals = []
marks = []
f1 = open("gk1.txt", "r")
for i in range(0, 10, 1):
    line1 = f1.readline().strip()
    list1 = line1.split(",")
    countries.append(list1[0])
    capitals.append(list1[1])

for i in range(0, 3, 1):
    r1 = input("What is the capital of "+countries[i])
    if r1.lower() == capitals[i].lower():
        marks.append(10)
    else:
        marks.append(0)
print(marks)
print(sum(marks))

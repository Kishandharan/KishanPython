str1 = "Funw"
str2 = " "

list1 = []
list2 = []

for x in range(len(str1)-1, 0, -1):
    temp1 = str2*x
    list1.append(temp1)

list1.append("")

for x in range(1, len(str1), 1):
    temp1 = str2*x
    list1.append(temp1)

for x in range(1, len(str1), 1):
    list2.append(str1[0:x])

list2.append(str1)

for x in range(len(str1)-1, 0, -1):
    list2.append(str1[0:x])


for x in range(0, len(list1), 1):
    print(list1[x], end="")
    print(list2[x])
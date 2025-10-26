f1 = open("menu.txt", "r")
f2 = open("order.txt", "r")

list1 = f1.readlines()
list2 = f2.readlines()

list3 = []
list4 = []
dict1 = dict()


for line in list1:
    temp = line.split(",")
    print(temp)
    list3.append(temp[0].strip())
    list4.append(temp[1].strip())

dict1 = dict(zip(list3, list4))

print(dict1)


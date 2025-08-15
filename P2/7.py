f1 = open("data.txt", "r")
str1 = f1.readline()
list1 = str1.split("*")[1:-1]
print(list1)

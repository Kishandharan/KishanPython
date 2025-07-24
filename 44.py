str1 = "Fun"
str2 = " "

list1=[]
list2=[]

for i in range(len(str1)-1, 0, -1):
    list1.append(str2*i)

list1.append(str2*0)

for i in range(1, len(str1), 1):
    list1.append(str2*i)

# ------------------------------

for i in range(1, len(str1), 1):
    list2.append(str1[0:i])

list2.append(str1)

for i in range(len(str1)-1, 0, -1):
    list2.append(str1[0:i])

for i in range(0, (len(str1)*2)-1, 1):
    print(list1[i]+list2[i])

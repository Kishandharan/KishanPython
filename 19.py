list1=[]
list2=[]
list3=[]

str1=input("START & STOP (seperated by whitespace): ")
str2=input("TABLE NUMS (seperated by whitespace): ")
list4=str1.split(" ")
list5=str2.split(" ")
start=list4[0]
end=list4[1]


for i in range(int(start), int(end)+1, 1):
    list1.append(f"{i}*{list5[0]}={int(list5[0])*i}")
    list2.append(f"{i}*{list5[1]}={int(list5[1])*i}")
    list3.append(f"{i}*{list5[2]}={int(list5[2])*i}")

for i in range(0, int(end), 1):
    print(list1[i], "                    ", list2[i], "                    ", list3[i])

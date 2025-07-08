f1=open("in4.txt", "r")
f2=open("out2.txt", "w")
s1=f1.readline()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
for j in range(n1,n2+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write("kishan")
        f2.write("\n")
    f2.write("\n")
    print()

f2.close()

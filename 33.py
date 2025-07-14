f1 = open("marks.txt", "r")
sub1 = []
sub2 = []
sub3 = []
sub4 = []
sub5 = []
marks1=[]
marks2=[]
logs1=[]
students=[]
toppers=[]

for j in range(0,26,1):
    line=f1.readline()
    temp=line.split(",")
    students.append(temp[0])
    marks1=temp[3:-1]
    for i in marks1:
        temp=int(i.split(":")[1])
        marks2.append(temp)
    sub1.append(marks2[0])
    sub2.append(marks2[1])
    sub3.append(marks2[2])
    sub4.append(marks2[3])
    sub5.append(marks2[4])
    marks1.clear()
    marks2.clear()

counter1=0
index1=[]
maxmark1=0
for i in sub1:
    if counter1==0:
        maxmark1=i
        index1.append(counter1)
    else:
        if i>maxmark1:
            maxmark1=i
            index1[0]=counter1
        else:
            pass
    counter1+=1

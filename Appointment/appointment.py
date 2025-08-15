name1 = []
salary1 = []
city1 = []
date1 = []
f1 = open("data.txt", "r")
lines = f1.readlines()
for line in lines:
    temp1 = line.split(",")
    name1.append(temp1[0])
    salary1.append(temp1[1])
    city1.append(temp1[2])
    date1.append(temp1[3])
template1 = "Dear $name, You have been appointed as Centre Head at $location with $salary. Please report for duty on $date"

for i in range(0, len(name1), 1):
    temp2 = template1.replace("$name", name1[i]).replace("$location", city1[i]).replace("$salary", salary1[i]).replace("$date", date1[i])
    print(temp2)
    print()

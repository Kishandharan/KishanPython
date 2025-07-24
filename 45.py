f1 = open("list2.txt", "r")
list1 = []
list2 = []
list3 = []
score = 0

for _ in range(0, 10, 1):
    line = f1.readline()
    list1.append(line.split(",")[0])
    list2.append(line.split(",")[1].replace("\n", ""))

for x in list1:
    temp1 = input(f"What is the capital city of {x}? ").strip().lower()
    list3.append(temp1)

print()
for x in range(0, len(list2), 1):
    if list2[x].lower().strip() != list3[x]:
        print(f"Your answer to question number {x+1} is incorrect, the correct answer is '{list2[x]}'")
    else:
        score += 10

print()
print(f"Your total score is {score}")
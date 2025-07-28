list1 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
spaces1 = ["",""," "," "," "," "," "]
spaces2 = [" "," "," "," ","","",""]
days1 = list()
days1.append([30, 31, 1, 2, 3, 4, 5])
days1.append([6, 7, 8, 9, 10, 11, 12])

for x in range(0, len(list1), 1):
    print(list1[x], end=" ")
print()

for y in range(0, len(days1[0]), 1):
    print(spaces1[y], days1[0][y], end=" ")
print()

for z in range(0, len(days1[1]), 1):
    print(spaces2[z], days1[1][z], end=" ")
print()



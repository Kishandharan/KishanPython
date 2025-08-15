# criteria1: it should be divisible by 4
# criteria2: if it is divisible by 4, you have to check if it is divisible by 100
# criteria3: if it is divisible by both 4 and 100, check if the number is divisible by 400
# criteria4: if it is divisible by 4 and not divisible by 100, we can say that is a leap year

list1 = list(range(2000, 2401, 1))
list2 = []
for i in list1:
    if i%4 == 0:
        if i%100 == 0:
            if i%400 == 0:
                list2.append(i)
        else:
            list2.append(i)

print(list2)


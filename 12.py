list1 = [7, 17, 9, 2, 8, 3]
list2 = []
lcn : int

for i in range(0, len(list1), 1):
    lcn = list1[i]
    if i == 0:
        if lcn < list1[i+1]:
            continue
        elif lcn < list1[i+2]:
            continue
        elif lcn < list1[i+3]:
            continue
        elif lcn < list1[i+4]:
            continue
        elif lcn < list1[i+5]:
            continue
        else:
            list2.append(lcn)
    if i == 1:
        if lcn < list1[i + 1]:
            continue
        elif lcn < list1[i + 2]:
            continue
        elif lcn < list1[i + 3]:
            continue
        elif lcn < list1[i + 4]:
            continue
        else:
            list2.append(lcn)
    if i == 2:
        if lcn < list1[i + 1]:
            continue
        elif lcn < list1[i + 2]:
            continue
        elif lcn < list1[i + 3]:
            continue
        else:
            list2.append(lcn)

    if i == 3:
        if lcn < list1[i + 1]:
            continue
        elif lcn < list1[i + 2]:
            continue
        else:
            list2.append(lcn)

    if i == 4:
        if lcn < list1[i + 1]:
            continue
        else:
            list2.append(lcn)
    if i == 5:
        list2.append(lcn)

print(list2)
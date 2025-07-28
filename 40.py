str1 = "right"
for x in range(0, len(str1), 1):
    print(''.join(list(str1)[0:x+1]))

for x in range(len(str1)-1, 0, -1):
    print(''.join(list(str1)[0:x]))
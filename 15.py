str1 = "I have the qwerty keyboard layout"
str2 = ""
list1 = str1.split()
for x in str1:
    for y in range(0,5):
        str2 += x

print(str2)

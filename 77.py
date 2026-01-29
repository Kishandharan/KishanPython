str1 = "ABCDEF"
str2 = ""
for i in range(1, 7, 1):
    str2 = str2+str1[6-i:7-i]
print(str2)


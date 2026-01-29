def reverse1(str1):
    str2 = ""
    len1 = len(str1)
    for i in range(1, len1+1, 1):
        str2 = str2+str1[len1-i:len1+1-i]
    return str2

result = reverse1("Fun with Programming")
print(result)

def diamondleft(str1):
    spaces = " "
    len1 = len(str1)

    for i in range(1, len1, 1):
        print((spaces*(len1-i))+str1[0:i])

    for i in range(0, len1, 1):
        print((spaces*i)+str1[0:len1-i])

diamondleft("Gayathri")
diamondleft("CS")

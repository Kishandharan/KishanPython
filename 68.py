def diamondright(str1):
    len1 = len(str1)
    for i in range(1, len1+1, 1):
        print(str1[0:i])
    for i in range(0, len1-1, 1):
        print(str1[0:len1-1-i])

diamondright("FunwithProgrammmingisabeautifulinternship")

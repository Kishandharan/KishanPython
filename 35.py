from random import randint
from random import shuffle

def genPwd1(pswd_len):
    str1 = "abcdefghijklmnopqrstuvwsyz"
    str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str3 = "1234567890"

    mastl = list(str1+str2+str3)
    list1 = list(str1)
    list2 = list(str2)
    list3 = list(str3)

    rand1 = randint(0, len(str1 )-1)
    rand2 = randint(0, len(str2 )-1)
    rand3 = randint(0, len(str3 )-1)
    rand4 = randint(0, len(mastl)-1)

    pswd1 = ""

    for x in range(0, pswd_len, 1):
        rand = randint(0, len(mastl)-1)
        pswd1 += mastl[rand]

    return pswd1

def genPwd2(pswd_len, pswd_qty):
    list1 = []
    for x in range(0, pswd_qty, 1):
        pwd = genPwd1(pswd_len)
        list1.append(pwd)
    return list1

print( genPwd2( 5, 5 ) )
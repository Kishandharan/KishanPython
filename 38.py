from random import randint

def genPwd1(pswd_len):
    list1 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    pswd1 = ""

    for x in range(0, pswd_len):
        rand1 = randint(0, len(list1)-1)
        pswd1 += list1[rand1]

    return pswd1

print( genPwd1( 1000 ) )
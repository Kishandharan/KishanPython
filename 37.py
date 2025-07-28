from random import randint

list1 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

rand1 = randint(0, len(list1)-1)
rand2 = randint(0, len(list1)-1)
rand3 = randint(0, len(list1)-1)

pswd = list1[rand1] + list1[rand2] + list1[rand3]

print(pswd)

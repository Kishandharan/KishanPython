from random import randint

list1 = list("abcdefghijklmnopqrstuvwxyz")
list2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
list3 = list("1234567890")

rand1 = randint(0, len(list1)-1)
rand2 = randint(0, len(list2)-1)
rand3 = randint(0, len(list3)-1)

pswd = list1[rand1] + list2[rand2] + list3[rand3]

print(pswd)
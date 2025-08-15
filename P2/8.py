from random import choice, shuffle
def genpwd1():
    pwd = ""
    numbers = list(range(0, 10, 1))
    upper_letters = []
    lower_letters = []
    for i in range(65, 91, 1):
        upper_letters.append(chr(i))
    for i in range(97, 123, 1):
        lower_letters.append(chr(i))
    choice1 = str(choice(numbers))
    choice2 = choice(upper_letters)
    choice3 = choice(lower_letters)
    list1 = list(choice1+choice2+choice3)
    shuffle(list1)
    for i in list1:
        pwd+=i
    print(pwd)

genpwd1()

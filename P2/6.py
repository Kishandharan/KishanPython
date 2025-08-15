from random import choice,shuffle
def genpwd(qty):
    upper_letters = []
    lower_letters = []
    numbers = []
    pwds = []
    for i in range(0, 10, 1):
        numbers.append(i)
    for i in range(65, 91, 1):
        upper_letters.append(chr(i))
    for i in range(97, 123, 1):
        lower_letters.append(chr(i))
    for i in range(0, qty+1):
        choice1 = choice(upper_letters)
        choice2 = choice(lower_letters)
        choice3 = str(choice(numbers))
        list1 = list(choice1+choice2+choice3)
        shuffle(list1)
        pwd = ""
        for i in list1:
            pwd += i
        pwds.append(pwd)
        pwd = ""
    return pwds

result = genpwd(100)
print(result)

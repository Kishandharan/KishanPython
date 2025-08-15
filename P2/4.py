import random
f1 = open("dictionary.txt")
list1 = []
marks1 = []
marks2 = []
for i in range(0, 58110, 1):
    s1 = f1.readline().replace("\n","")
    list1.append(s1)

for x in range(4):
    user_Choice = input("You: ")
    lastletter = user_Choice[-1]
    comp_Choice = random.choice(list(filter(lambda x: x.startswith(lastletter), list1)))
    len1 = len(user_Choice)
    len2 = len(comp_Choice)
    marks1.append(len1)
    marks2.append(len2)
    print(user_Choice," - ",comp_Choice, len1, len2)
'''
rule1 - User should input before 30 secs
rule2 - User's starting letter should as same as computer's last letter
rule3 - User should nt repeat words already used in the game
rule4 - User should enter words present in English dictionary

'''
print(sum(marks1))
print(sum(marks2))


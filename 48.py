import random
f1 = open("dictionary.txt", "r")
words = []
for i in range(0, 58110, 1):
    words.append(f1.readline().replace("\n",""))
lcc = ""
while True:
    userChoice = input("You: ")
    temp1 = []
    if not userChoice.startswith(lcc[-1]):
        break        
    
    if(userChoice not in words):
        break
    
    for i in words:
        if i.startswith(userChoice[-1]):
            temp1.append(i)
    computerChoice = random.choice(temp1)
    print("Computer:", computerChoice)
    lcc = computerChoice

print("------------------------ GAME OVER ------------------------")        


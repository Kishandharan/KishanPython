import random
from inputimeout import inputimeout
f1 = open("dictionary.txt", "r")
words = [i.replace("\n", "") for i in f1.readlines()]
userChoice = ""
compChoice = ""
try:
	userChoice = inputimeout(prompt="You: ", timeout=10) 
	lastletter1 = userChoice[-1]
	filtered_words = list(filter(lambda x: True if x.startswith(lastletter1) else False, words))
	compChoice = random.choice(filtered_words)
	lastletter2 = compChoice[-1] 
	print("Comp:", compChoice)

	for i in range(0, 3, 1):
		userChoice = inputimeout(prompt="You: ", timeout=10)
		if userChoice.startswith(lastletter2) and (userChoice in words):
			lastletter1 = userChoice[-1]
			filtered_words = list(filter(lambda x: True if x.startswith(lastletter1) else False, words))
			compChoice = random.choice(filtered_words)
			lastletter2 = compChoice[-1] 
			print("Comp:", compChoice)
		else:
			break
except:
	print("Reason:")
	print("You took too long to respond")
	print("------- GAME OVER -------")

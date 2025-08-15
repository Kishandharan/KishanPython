import random
choices = ["rock", "paper", "scissor"]

for i in range(0, 11, 1):
	p1 = input("You -- ").lower()
	p2 = random.choice(choices)
	print("Computer --", p2)

	if p1 == "rock":
		match(p2):
			case "rock":
				print("It's a tie!")

			case "paper":
				print("Computer won!")

			case "scissor":
				print("You won!")

	elif p1 == "paper":
		match(p2):
			case "rock":
				print("You won!")

			case "paper":
				print("It's a tie")

			case "scissor":
				print("Computer won!")

	elif p1 == "scissor":
		match(p2):
			case "rock":
				print("Computer won!")

			case "paper":
				print("You won!")

			case "scissor":
				print("It's a tie!")
	else:
		break
	print("\n")


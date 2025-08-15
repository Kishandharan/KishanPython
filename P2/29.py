li1 = [
	{
        "ques": "What is the capital of France?",
        "options" : ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "ans": 3
    },
    {
        "ques": "Who wrote 'Hamlet'?",
        "options" : ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain", "4. J.K. Rowling"],
        "ans": 2
    },
    {
        "ques": "What is the largest planet in our solar system?",
        "options" : ["1. Earth", "2. Jupiter", "3. Mars", "4. Saturn"],
        "ans": 2
    }
]

score = 0
level = ""
for i in li1:
	print(i["ques"])
	for j in i["options"]:
		print(j)
	answer = int(input("CORRECT OPT NUM>> "))
	if answer < 5 and answer > 0:
		if answer == i["ans"]:
			print(":)")
			score+=1
		else:
			print(":(")
	else:
		print("Out of range!!")
	print()

print(f"Your score : {score}")
if score >= 0 and score <= 2:
	level = "Garbage"
else:
	level = "Very Rare"
print(f"Your performance is like: {level}")
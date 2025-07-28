from inputimeout import inputimeout, TimeoutOccurred
import random
import sys
################################
dictionary_file = open("dictionary.txt", "r")
dictionary1 = dictionary_file.readlines()
dictionary2 = []
comp_word = ""
user_word = ""
user_last_char = ""
comp_last_char = ""
user_score = 0
timeout = 10
while True:
    try:
        rounds = int(input("How many rounds do you want to play? >> "))
        break
    except ValueError:
        print("Hmm! it looks like you have entered something invalid to this prompt!")
        print("Let's try again!")
        print()
print("Alright, let's start!")
print()

for x in dictionary1:
    word = x.replace("\n", "")
    dictionary2.append(word)

for x in range(0, rounds, 1):
    if x == 0:
        comp_word = random.choice(dictionary2)
        comp_last_char = comp_word[-1]
        print("Comp >>", comp_word)
    else:
        possible_comp_words = list(filter(lambda y: y.startswith(user_last_char), dictionary2))
        comp_word = random.choice(possible_comp_words)
        comp_last_char = comp_word[-1]
        print("Comp >>", comp_word)

    try:
        user_word = inputimeout(prompt="User >> ", timeout=timeout)
    except TimeoutOccurred:
        print("Oops, you lost! Because you took too long to respond!")
        print(f"The maximum amount of time you can take to respond is {timeout} secs.")
        print(f"Here is your score: {user_score}")
        sys.exit()

    user_last_char = user_word[-1]
    if user_word.startswith(comp_last_char) and (user_word in dictionary2):
        user_score += 1
    else:
        print()
        print("Oops, you lost!")
        print(f"Here is your score: {user_score}")
        sys.exit()

print()
print("Good job! You have gone through all the rounds!")
print(f"Here is your score: {user_score}")


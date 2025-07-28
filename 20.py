vowels = ["a", "e", "i", "o", "u"]
word = input("Word: ")
new_word = ""

for i in word:
    if i in vowels:
        new_word += chr(ord(i)+5)
    else:
        new_word += chr(ord(i)+4)
print(new_word)

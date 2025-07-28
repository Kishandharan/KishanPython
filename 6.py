text1 = input("Enter something: ")
tt1 = ""
list1 = []

if len(text1) > 33:
    list1 = text1.split(" ")
    tt1 = f"{list1[0]} {list1[1]}...{list1[-1]}"

print(tt1)
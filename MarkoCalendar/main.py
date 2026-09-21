from datetime import datetime as dt

now = dt.now()
year = now.year
month = now.month
date = now.day

while True:
    cmd1 = input(">> ")
    cmd2 = cmd1.strip() 
    first_term = cmd2.split(" ")[0]

    if first_term == "mark":
        print("You said mark")

    elif first_term == "exit":
        print("Bye bye!")
        break
    
    else:
        if len(first_term) != 0:
           print("Invalid command") 

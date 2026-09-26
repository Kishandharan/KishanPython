from datetime import datetime as dt
import os

now = dt.now()
year = now.year
month = now.month
date = now.day

month_num_to_name = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

while True:
    cmd1 = input(">> ")
    cmd2 = cmd1.strip() 
    first_term = cmd2.split(" ")[0]

    if first_term == "init":
        if os.path.isfile(".mc_data"):
            print("Already initialized")
        else:
            f1 = open(".mc_data", "w")
            f2 = open(".mc_remove", "w")
            f1.close()
            f2.close()
       
    elif first_term == "show_day":
        print(f"\nYear: {year}")
        print(f"Month: {month_num_to_name[month]}")
        print(f"Date: {date}\n")

    elif first_term == "exit":
        print("Bye bye!")
        break
    
    else:
        if len(first_term) != 0:
           print("Invalid command") 

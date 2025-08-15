from inputimeout import inputimeout
# import time
# import datetime as dt 

# for i in range(0, 10, 1):
# 	today = dt.datetime.now()
# 	print(today)
# 	time.sleep(2)
try:
	data = inputimeout(prompt="Enter your name: ", timeout=6)
	print("Thank you, your lastletter is -", data[-1])
except Exception:
	print("Sorry, game is over, you have lost!")


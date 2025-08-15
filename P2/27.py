from threading import Thread
import time

def step1():
	time.sleep(3)
	print("1")

def step2():
	time.sleep(2)
	print("2")

def step3():
	time.sleep(1)
	print("3")

thread1 = Thread(target=step1)
thread2 = Thread(target=step2)
thread3 = Thread(target=step3)

thread1.start()
thread2.start()
thread3.start()

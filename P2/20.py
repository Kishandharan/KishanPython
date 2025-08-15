def addBehavior(func):
	def wrapper():
		print("Added behavior")
		func()
	return wrapper

@addBehavior
def func1():
	print("Default behavior")

func1()

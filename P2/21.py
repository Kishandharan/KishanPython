def addSprinkles(func):
	def wrapper():
		print("Add Sprinkles")
		func()
	return wrapper

@addSprinkles
def getIceCream():
	print("Here is your ice cream")

getIceCream()


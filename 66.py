class Memoizer:
    mem = {}
    def run(self, function, arguments):
        if arguments in self.mem.keys():
            print("Memoized")
            return self.mem.get(arguments)
        else:
            print("Calculated")
            result = function(*arguments)
            self.mem[arguments] = result 

memoizerObj = Memoizer()

def fact(num1):
    num1C = num1
    for i in range(num1C-1, 0, -1):
        num1C = num1C * i
    return num1C


num1 = memoizerObj.run(fact, (1000, ))
num2 = memoizerObj.run(fact, (1000, ))

print(num1)
print(num2)


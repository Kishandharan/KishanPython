class Memoizer:
    mem = {}
    def run(self, function, arguments):
        if arguments in self.mem.keys():
            print("Memoized Value")
            return self.mem.arguments
        else:
            print("Calculated Value")
            return function(*arguments)

memoizerObj = Memoizer()

def mult(num1, num2):
    return num1*num2

memoizerObj.run(mult, [10, 10])
memoizerObj.run(mult, [10, 10])

def greet(func):
    print("Decorator applied")
    def wrapper():
        print(f"Hi Person!")
        func()
        print(f"Bye Person!")
    return wrapper

@greet
def doSomething():
    for i in range(1, 11):
        print(f"    Count: {i}")

@greet
def doSomethingElse():
    for i in range(10, 21):
        print(f"    Count: {i}")


print()
print()

doSomething()
doSomethingElse()

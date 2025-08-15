def func1():
    print("Starting func1")
    func2()
    print("Ending func1")

def func2():
    print("Starting func2")
    print("Hello")
    print("Ending func2")

func1()
def factorial(num):
    copyNum = num
    for i in range(copyNum-1, 0, -1):
        copyNum = copyNum * i

    return copyNum

print(factorial(5000000000))

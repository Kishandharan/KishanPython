list1 = [0, 1] # Fibonacci Series
num1, num2 = 0, 1
sum1 = num1+num2
list1.append(sum1)

for i in range(0, 20, 1): 
    num1 = num2
    num2 = sum1
    sum1 = num1+num2
    list1.append(sum1)
print(list1)

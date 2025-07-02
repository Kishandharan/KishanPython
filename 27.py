num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
oper = input("Enter an operator: ")

if oper == "+":
    print(num1+num2) 
elif oper == "-":
    print(num1-num2) 
elif oper == "*":
    print(num1*num2) 
elif oper == "/":
    print(num1//num2)
else:
    print("Oopsie! Ypu have entered an invalid input! Please try again!!!")

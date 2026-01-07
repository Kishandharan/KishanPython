# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,

list1 = [2,3]
print(list1)
for j in range(4, 1000, 1):
    num1 = j
    isPrime = True
    for i in range(2, j, 1):
        if num1%i==0:
            isPrime=False
    if isPrime==True:
        list1.append(num1)
print(list1)  


from django.shortcuts import render

def home(request):
    result=fact(10)
    return render(request,'app1/index.html',{'param1':result})

def fact(num1):
    result=num1 # 5
    for i in range(result, 1, -1):
        result=result*i

    return result

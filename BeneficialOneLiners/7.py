def greater_than_two(x):
    if x > 2:
        return True

list1 = [1,5,6,7,2,3]
list2 = list(filter(greater_than_two, list1))
print(list2)
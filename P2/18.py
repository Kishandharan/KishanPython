def oly1(fname):
    f1 = open(fname, 'r')
    li1 = []
    flags = []
    for x in range(10):
        s1 = f1.readline().replace('\n','')
        li2 = s1.split(',')
        flags.append("images/"+li2[0]+".png")
        li1.append(li2)
    return (li1,flags)
fname = 'olympics.csv'
result = oly1(fname)
print(result[0])
print(result[1])


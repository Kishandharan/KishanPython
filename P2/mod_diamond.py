def diamond1(s1):
    len1=len(s1)
    for i in range(1,len1+1,1):    
        s2=s1[0:i]
        print(s2)
    for i in range(1,len1,1):    
        s2=s1[0:len1-i]
        print(s2)

if __name__ == '__main__':
    diamond1('AshwinMangalore')    
    diamond1('Chandrashekar')

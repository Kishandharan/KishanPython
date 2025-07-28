import os
walk=list(os.walk(top=os.getcwd()))
virus_signatures = open("signature.txt", "r")
virus_strs=[]
for x in virus_signatures.readlines():
    virus_strs.append(x.lower().strip())
for x in walk:
    os.chdir(x[0])
    for y in x[-1]:
        f1=open(y, "r")
        if f1.read().lower() in virus_strs:
            print(f"The file {x[0]+"\\"+y} seems to be malicious. Please delete it.")
         
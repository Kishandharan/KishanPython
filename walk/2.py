import os
walk=list(os.walk(top=os.getcwd()))
virus_strs=["I will destroy YOU! HAHAHAHAHAHAHA!", "I am a RAKSHASA, HAHAHAHA!"]
for x in walk:
    os.chdir(x[0])
    for y in x[-1]:
        f1=open(y, "r")
        if f1.read() in virus_strs:
            print(f"The file {x[0]+"\\"+y} seems to be malicious. Please delete it.")
         
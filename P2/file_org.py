'''
In order to use this utility, make sure that python is installed.
If not visit https://www.python.org/downloads/.
After downloading this file, open cmd in the place where this file is downloaded. Then in the opened cmd, type file_organizer.py path_to_be_organized extension_to_be_filtered.

'''
import os
import shutil
import sys
#############################################
path = sys.argv[1]
ext = sys.argv[2]
dir_name = f"{ext} files"
os.chdir(path)
list1 = os.listdir()
if not os.path.isdir(dir_name):
	os.mkdir(dir_name)
for i in list1:
	if (i.endswith(ext)) and (os.path.isfile(i)):
		shutil.move(i, path+"\\"+dir_name)

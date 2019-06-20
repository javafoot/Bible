#!/bin/env python3

from datetime import datetime
import os
import re

pyfile = os.path.abspath(__file__)
print(pyfile)
pydir = os.path.dirname(pyfile)
filename = pydir + "/scripture.txt"
print(filename)
with open(filename,encoding='UTF-8') as f:
    scripture = f.read()

##print(scripture)

now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
all = f'{mm}月{dd}号感动经文:\n\n'
line = re.sub(r'[\n\s]+|（.+?）','',scripture)
cleanStr = re.sub(r'和合本\)',r")\n\n",line)
all += cleanStr


print(all)
print("777LJC777")

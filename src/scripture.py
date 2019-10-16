#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====

from datetime import datetime
import os
import re

linesep = os.linesep
## /swd/code>ln -s /swd/code/t01/t02/test.py 0t.py
## os.path.realpath(__file__)  ## /swd/code/0t.py
## os.path.abspath(__file__)   ## /swd/code/t01/t02/test.py
pyfile = os.path.abspath(__file__)
print(pyfile)
##pydir = os.path.dirname(pyfile)
##filename = pydir + "/scripture.txt"
filename = pyfile + '.txt'
print(filename)
with open(filename,encoding='UTF-8') as f:
    scripture = f.read()

##print(scripture)

now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
allStr = f'{mm}月{dd}号感动经文:{linesep}{linesep}'
line = re.sub(r'[\n\s]+|（.+?）','',scripture)
cleanStr = re.sub(r'和合本\)',r')\n\n',line)
allStr += cleanStr


print(allStr)
print("777LJC777")

##==== Glory to GOD ====


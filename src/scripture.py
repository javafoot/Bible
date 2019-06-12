#!/bin/env python

from datetime import datetime
import re


#filename = "scripture.txt"
filename = "/storage/emulated/0/documents/scripture.txt"
with open(filename,encoding='UTF-8') as f:
    scripture = f.read()

print(scripture)

now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
all = f'{mm}月{dd}号感动经文:'
line = re.sub(r'[\n\s]+|（.+）','',scripture)
cleanStr = re.sub(r'和合本\)',r")\n\n",line)
#all += '\n\n'
all += cleanStr
    
print(all)
print(111)

#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

scripture = '''所以你当归向你的　神，谨守仁爱、公平，常常等候你的　神。(何西阿书 12:6 和合本)But you must return to your God; maintain love and justice, and wait for your God always. (Hosea 12:6 NIV)'''

linesep = os.linesep
now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
allSc = f'{mm}月{dd}号背诵金句: '  ## 08月27号背诵金句: 126415  9147

chEng = scripture.split('和合本)')  ## Seperate Chinese from English
chs = re.sub(r'[\n\s]+|（.+?）','',chEng[0]) + ')'  ## Clean Chinese part

## Count Chinese characters
chsParts = re.split(r'[，。；－”]+',chs)
print(chsParts)
count = ""
for part in chsParts:
    if part.startswith('('):
        continue
    partWithoutPuncMark = re.sub(r'、','',part)  ## Remove the punctuation marks like '、' before counting.
    count += str(len(partWithoutPuncMark))
    
print(count)

## Handle Eng
eng = re.sub(r'\s*\(((?:[12] )?\w+) ([\d:]+) NIV\)',r'(\1\2)',chEng[1])  ## Handle the part '. (2 Kings 19:18 NIV)'
eng = re.sub(linesep+'*','',eng)  ## Clean Eng part

## Count Eng words
engParts = re.split(r'[,.;]',eng)
count += "  "
for part in engParts:
    if part.startswith('('):
        continue
    #print(part.strip().split(' '))
    count += str(len(part.strip().split(' ')))
allSc += count + linesep + linesep + chs + linesep + eng
print(allSc)
##==== Glory to GOD ====


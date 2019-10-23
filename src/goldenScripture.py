#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

scripture = '''

原来我们在许多事上都有过失；若有人在话语上没有过失，他就是完全人，也能勒住自己的全身。 (雅各书 3:2 和合本)We all stumble in many ways. Anyone who is never at fault in what they say is perfect, able to keep their whole body in check. (James 3:2 NIV)


'''


'''“基督耶稣降世，为要拯救罪人。”这话是可信的，是十分可佩服的。在罪人中我是个罪魁。 (提摩太前书 1:15 和合本)Here is a trustworthy saying that deserves full acceptance: Christ Jesus came into the world to save sinners—of whom I am the worst. (1 Timothy 1:15 NIV)'''

linesep = os.linesep
now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
allSc = f'{mm}月{dd}号背诵金句: '  ## 08月27号背诵金句: 126415  9147

chEng = scripture.split('和合本)')  ## Seperate Chinese from English

## Handle Chinese
chs = re.sub(r'[\n\s]+|（.+?）','',chEng[0]) + ')'  ## Clean Chinese part
## Count Chinese characters
chsParts = re.split(r'[，。；－：”]+',chs)
print(chsParts)
count = ""
for part in chsParts:
    if part.startswith('('):
        continue
    partWithoutPuncMark = re.sub(r'[、“”]','',part)  ## Remove the punctuation marks like '、' before counting.
    count += str(len(partWithoutPuncMark))
print(count)

## Handle Eng
eng = re.sub(r'\s*\(((?:[12] )?\w+) ([\d:]+) NIV\)',r'(\1\2)',chEng[1])  ## Handle the part '. (2 Kings 19:18 NIV)'
eng = re.sub(linesep+'*','',eng)  ## Clean Eng part
## Count Eng words
engParts = re.split(r'[,.;]|: “|”—',eng)
print(engParts)
count += "  "
for part in engParts:
    if part.startswith('('):
        continue
    #print(part.strip().split(' '))
    cleanPart = re.sub(r'[、“”]','',part).strip()
    count += str(len(cleanPart.split(' ')))
allSc += count + linesep + linesep + chs + linesep + eng
print(allSc)
##==== Glory to GOD ====


#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

scripture = '''

因今天在大卫的城里，为你们生了救主，就是主基督。你们要看见一个婴孩，包着布，卧在马槽里，那就是记号了。 (路加福音 2:11-12 和合本)
Today in the town of David a Savior has been born to you; he is the Messiah, the Lord. This will be a sign to you: You will find a baby wrapped in cloths and lying in a manger. (Luke 2:11-12 NIV)


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
chsParts = re.split(r'[，。；－：”？]+',chs)
print(chsParts)
count = ""
for part in chsParts:
    if part.startswith('('):
        continue
    partWithoutPuncMark = re.sub(r'[、“”]','',part)  ## Remove the punctuation marks like '、' before counting.
    count += str(len(partWithoutPuncMark))
print(count)

## Handle Eng
eng = re.sub(r'\s*\(((?:[12] )?\w+) ([\d:-]+) NIV\)',r'(\1\2)',chEng[1])  ## Handle the part '. (2 Kings 19:18 NIV)'
eng = re.sub(linesep+'*','',eng)  ## Clean Eng part
## Count Eng words
engParts = re.split(r'[,.;?:]|: “|”—',eng)
print(engParts)
count += "  "
for part in engParts:
    if part.startswith('(') or part.endswith(')'):
        continue
    #print(part.strip().split(' '))
    cleanPart = re.sub(r'[、“”]','',part).strip()
    count += str(len(cleanPart.split(' ')))
allSc += count + linesep + linesep + chs + linesep + eng
print(allSc)
##==== Glory to GOD ====


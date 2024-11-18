#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

scripture = '''

因有一婴孩为我们而生；有一子赐给我们。政权必担在他的肩头上；他名称为“奇妙策士、全能的　神、永在的父、和平的君”。(以赛亚书 9:6 和合本)
For to us a child is born, to us a son is given, and the government will be on his shoulders. And he will be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace. (Isaiah 9:6 NIV)


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


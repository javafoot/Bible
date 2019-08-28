#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

scripture = '''将列国的神像都扔在火里；因为它本不是神，乃是人手所造的，是木头石头的，所以灭绝它。 (列王纪下 19:18 和合本)
They have thrown their gods into the fire and destroyed them, for they were not gods but only wood and stone, fashioned by human hands. (2 Kings 19:18 NIV)'''

linesep = os.linesep
now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
allSc = f'{mm}月{dd}号背诵金句: '  ## 08月27号背诵金句: 126415  9147

chEng = scripture.split('和合本)')  ## Seperate Chinese from English
chs = re.sub(r'[\n\s]+|（.+?）','',chEng[0]) + ')'  ## Clean Chinese part

## Count Chinese characters
chsParts = re.split(r'[，。；－]',chs)
count = ""
for part in chsParts:
    if part.startswith('('):
        continue
    count += str(len(part))
    
#print(count)

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


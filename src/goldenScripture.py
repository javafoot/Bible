#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re

linesep = os.linesep
scripture = '''耶和华－你　神原是有怜悯的　神；他总不撇下你，不灭（不撇下你，不）绝你，也不忘记他起誓   与你列祖所立的约。  (申命记 4:31 和合本)
For the Lord your God is a merciful God; he will not abandon or destroy you or forget the covenant with your ancestors, which he confirmed to them by oath.  (Deuteronomy 4:31 NIV)'''


now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
allSc = f'{mm}月{dd}号背诵金句: '
#08月27号背诵金句: 126415  9147

chEng = scripture.split('和合本)')
chs = re.sub(r'[\n\s]+|（.+?）','',chEng[0]) + ')'

chsParts = re.split(r'[，。；－]',chs)
count = ""
for part in chsParts:
    if part.startswith('('):
        continue
    count += str(len(part))
    
#print(count)
allSc += count + linesep + linesep + chs + linesep
#print(allSc)
eng = re.sub(r'\s*\((\w+) ([\d:]+) NIV\)',r'(\1\2)',chEng[1])
eng = re.sub(linesep+'*','',eng)
allSc += eng
#print(eng)
#print(1111111111)
print(allSc)
exit()
result = re.match(r'(.+)\(.+和合本\)(.+)',scripture)
print(result)
if True:
    quit()
now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
all = f'{mm}月{dd}号背诵金句: '

line = re.sub(r'[\n\s]+|（.+）|和合本|NIV','',scripture)
parts = re.split('[；，。]',line)
for part in parts:
    cleanStr = re.sub(r'[：“、…]','',part)
    account = str(len(cleanStr))
    all += account
    print(account,part)
print(all)



###
# re.subn(r'\(.+?\)\s*','',sc)
##('Let us not become weary in doing good, for at the proper time we, will reap a harvest if we do not give up. ', 2)
'''
ss='Let us not become weary in doing good, for at the proper time (right time) we(good), will reap a harvest if we do not give up. (Galatians 6:9 NIV)'


chapNoPtn = re.compile(r'\(\w+\s*\d+:\d+(?:-\d+)?(?:\s+NIV)?\)')
chapNoPtn.findall(ss)
['(Galatians 6:9 NIV)']
>>> chapNoPtn.sub('',ss)
'Let us not become weary in doing good, for at the proper time (right time) we(good), will reap a harvest if we do not give up. '
>>> sc = chapNoPtn.sub('',ss)
>>> sc
'Let us not become weary in doing good, for at the proper time (right time) we(good), will reap a harvest if we do not give up. '

>>> re.sub(r'\(.+?|)\s','',sc)
>>> re.sub(r'\(.+?\)\s','',sc)
'Let us not become weary in doing good, for at the proper time we(good), will reap a harvest if we do not give up. '
>>> re.subn(r'\(.+?\)\s*','',sc)
('Let us not become weary in doing good, for at the proper time we, will reap a harvest if we do not give up. ', 2)


'''
##==== Glory to GOD ====


#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import re

scripture = '''
道成了肉身住在我们中间，充充满满的有恩典有真理。我们也见过他的荣光，正是父独生子的荣光。 (约翰福音 14:2-3,6,13 和合本)The Word became flesh and made his dwelling among us. We have seen his glory, the glory of the One and Only, who came from the Father, full of grace and truth. (John 14:2-3,6,13 NIV)'''

#print(scripture)
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


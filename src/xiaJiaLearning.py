#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====

from datetime import datetime
import os
import re

linesep = os.linesep
pyfile = os.path.abspath(__file__)
print(pyfile)
filename = pyfile + '.txt'
print(filename)
with open(filename,encoding='UTF-8') as f:
    title = f.readline()
    content = f.read()

content = content.replace('','● ')

now = datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
title = f'{mm}.{dd} {title.strip()}:\n'
print(title)
print(content)
print("777LJC777")

##==== Glory to GOD ====





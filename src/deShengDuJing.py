#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime
import os,re


date = 23
books = ('诗篇','彼得后书','以西结书')
chapNo = (114,1,33)

days = 7
linesep = os.linesep
now = datetime.now()
mm = now.strftime('%m')
##dd = now.strftime('%d')
title = f'《得胜读经计划》{mm}月dd号读经：'  ## 《得胜读经计划》10月23号读经：
span = 0
while span < days:
    plan = title.replace('dd',str(date + span))
    plan += linesep + linesep
    for i in range(len(books)):
        if i < 2:
            plan += books[i] + str(chapNo[i] + span) + linesep
        else:
            start = chapNo[i] + span * 2
            plan += books[i] + str(start) + '-' + str(start + 1) + linesep
    span += 1
    print(plan)
    print("\n-----------\n\n")


##==== Glory to GOD ====


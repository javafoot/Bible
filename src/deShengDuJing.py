#!/bin/env python3
# -*- coding: UTF-8 -*-
##==== LORD JESUS CHRIST LOVES YOU ====
##==== Code in the Name of LORD JESUS CHRIST ====
from datetime import datetime,timedelta
import os,re

## [[<< Change the metadata -----------
month = 12 ##None
day = 28
books = ('箴言','腓立比书','约伯记')
chapNo = (29,1,38)
## >>]] Change the metadata -----------
days = 7
linesep = os.linesep
startTime = datetime.now()
if day != None:
    startTime = startTime.replace(day=day)
if month != None:
    startTime = startTime.replace(month=month)

span = 0
while span < days:
    theDay = startTime + timedelta(days=span)
    mm = theDay.strftime('%m')
    dd = theDay.strftime('%d')
    ##dd = now.strftime('%d')
    plan = f'《得胜读经计划》{mm}月{dd}号读经：'  ## 《得胜读经计划》10月23号读经：
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





https://web.xiaodaka.com/#/topic_list?habitID=1750228&currentPage=NaN







##==== Glory to GOD ====


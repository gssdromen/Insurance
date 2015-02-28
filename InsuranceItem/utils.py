# coding:utf-8

from datetime import date

def getDateFromString (datestr):
    datestr = str(datestr)
    if datestr == '':
        return ''
    temp = datestr.split('/')
    if len(temp) == 1:
        temp = datestr.split('-')
    for num in temp:
        if num[0] == '0':
            num = num[1:]
    year = int(temp[0])
    month = int(temp[1])
    day = int(temp[2])
    return date(year,month,day)

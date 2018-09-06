# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/26 21:33'

from ParseExcel import ParseExcel

pe=ParseExcel()

def findRowByName(sheetobj,targetName):
    names=pe.getColumn(sheetobj,2)
    count=0
    for i in names:
        count+=1
        if targetName==i.value:
            return count
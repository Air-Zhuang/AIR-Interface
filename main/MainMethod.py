# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/26 22:04'

from config.config import *
from util.ParseExcel import ParseExcel
from util.requestMethod import post,get
from util.findRowByName import findRowByName
from jsonpath_rw import parse
import json

pe=ParseExcel()
pe.loadWorkBook(excelPath)
sheetobj=pe.getSheetByName(sheetName)
#总行数
rowNum=pe.getRowsNumber(sheetobj)

def MainMethod():
    for i in range(2,rowNum+1):
        pe.writeCell2(sheetobj,"",rowNo=i,colsNo=colCode)
        pe.writeCell2(sheetobj, "", rowNo=i, colsNo=colResponse)
        pe.writeCell2(sheetobj, "", rowNo=i, colsNo=colPerformance)
        pe.writeCell2(sheetobj, "", rowNo=i, colsNo=colRunTime)
        pe.saveFile()
        if(pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colExecute))=="n":
            continue
        elif(pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colExecute))=="y":
            typee=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colType)
            urll=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colUrl)
            headerr=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colHeader)
            cookiee=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colCookie)
            bodyy=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colBody)
            dependNamee=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colDependName)
            parsee=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colParse)
            changee=pe.getCellOfValue(sheetobj,rowNo=i,colsNo=colChangeStr)
            #处理接口依赖
            if dependNamee:
                dependRow=findRowByName(sheetobj,dependNamee)   #获取依赖第几行
                dependResponse=pe.getCellOfValue(sheetobj,rowNo=dependRow,colsNo=colResponse)   #获取Excel上的response

                json_obj=json.loads(dependResponse) #转换成dict格式
                jsonpath_expr=parse(parsee)
                targetDepends=jsonpath_expr.find(json_obj)
                targetDepend=[match.value for match in targetDepends]   #得到依赖数据单个数据列表

                bodyy2=json.loads(bodyy) #将输入的bodyy的值改为目标依赖数据值
                bodyy2[changee]=targetDepend[0]
                bodyy3=json.dumps(bodyy2)
                bodyy=bodyy3
            if typee=="post":
                res,runtime=post(headers=headerr,url=urll,data=bodyy,cookie=cookiee)
                if str(res.status_code).startswith("2"):
                    style="green"
                elif str(res.status_code).startswith("3"):
                    style="yellow"
                else:
                    style="red"
                print res.status_code
                pe.writeCell(sheetobj,runtime,rowNo=i,colsNo=colPerformance,style="purple")
                pe.writeCell(sheetobj,res.status_code,rowNo=i,colsNo=colCode,style=style)
                pe.writeCell(sheetobj,res.text,rowNo=i,colsNo=colResponse,style=style)
                pe.writeCellCurrentTime(sheetobj,rowNo=i,colsNo=colRunTime)
            elif typee=="get":
                res,runtime=get(headers=headerr,url=urll,cookie=cookiee)
                if str(res.status_code).startswith("2"):
                    style="green"
                elif str(res.status_code).startswith("3"):
                    style="yellow"
                else:
                    style="red"
                print res.status_code
                pe.writeCell(sheetobj, runtime, rowNo=i, colsNo=colPerformance, style="purple")
                pe.writeCell(sheetobj, res.status_code, rowNo=i, colsNo=colCode, style=style)
                pe.writeCell(sheetobj, res.text, rowNo=i, colsNo=colResponse, style=style)
                pe.writeCellCurrentTime(sheetobj, rowNo=i, colsNo=colRunTime)
if __name__ == '__main__':
    MainMethod()




















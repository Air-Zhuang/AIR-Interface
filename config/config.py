# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/26 21:55'

import os

excelPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Interface.xlsx"
sheetName='Sheet1'

colNum=1            #序号
colName=2           #接口名
colUrl=3            #URL
colType=4           #请求类型
colHeader=5         #header
colCookie=6         #cookie
colBody=7           #body
colDependName=8     #依赖的接口名
colParse=9          #parse表达式
colChangeStr=10     #改变的字段
colCode=12          #状态码
colResponse=13      #返回数据
colExecute=11       #是否执行
colPerformance=14   #接口响应
colRunTime=15       #运行时间

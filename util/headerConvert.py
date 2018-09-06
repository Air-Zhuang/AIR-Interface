# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/26 21:41'

def headerConvert(header):
    headers=str(header).split("\n")
    dict1={}
    for i in range(len(headers)):
        dict1[headers[i].split(":")[0]]=headers[i].split(":")[1]
    return dict1
# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/26 21:45'

import requests
from cookieConvert import cookieConvertFromStrToDict
from headerConvert import headerConvert
import datetime

def post(headers,url,data,cookie=None):
    data2=(str(data))
    if str(headers).startswith("{"):
        headers2=dict(eval(headers))
    else:
        headers2=headerConvert(headers)
        # print headers2
    if cookie:
        cookie=cookieConvertFromStrToDict(cookie)
    starttime=datetime.datetime.now()
    res=requests.post(url=url,data=data2,headers=headers2,cookies=cookie,verify=False)
    endtime=datetime.datetime.now()
    runtime=str(endtime-starttime)
    return res,runtime

def get(headers,url,cookie=None):
    if str(headers).startswith("{"):
        headers2=dict(eval(headers))
    else:
        headers2=headerConvert(headers)
    if cookie:
        cookie=cookieConvertFromStrToDict(cookie)
    starttime = datetime.datetime.now()
    res = requests.get(url=url, headers=headers2, cookies=cookie, verify=False)
    endtime = datetime.datetime.now()
    runtime = str(endtime - starttime)
    return res, runtime
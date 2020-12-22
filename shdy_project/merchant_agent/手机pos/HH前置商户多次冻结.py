# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/2/25 10:33
import requests

url = 'http://192.168.31.161:18280/merchant_agent/rest/merchantInfo/updateMercStatus'
data = {
    "mercId":"101121155920001",
    "stlStatus":"1" #状态  0开启1关闭
}
req= requests.post(url,json=data).json()
print(req)

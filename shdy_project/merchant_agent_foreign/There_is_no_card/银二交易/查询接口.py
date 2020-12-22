# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/17 11:21
import requests
from SHDY.public import The_random_number
from SHDY.public.conf_test import Config

order_no = The_random_number.order_number()
dy_mch_no = Config().get_param("mercid")
dy_mch_no1 = Config().get_param("id")
mer_order_no = Config().get_param('mer_order_no')
url = 'https://116.228.47.74:7443/transaction_agent/payBack/trans'
data ={
    "org_no": "121",
    "dy_mch_no": dy_mch_no,
    "mer_order_no": mer_order_no,           #下单流水号
    "order_no":order_no ,
    "service": "query",
    "sign": "121212"

}

re = requests.post(url,json=data,verify=False).json()
print(re)
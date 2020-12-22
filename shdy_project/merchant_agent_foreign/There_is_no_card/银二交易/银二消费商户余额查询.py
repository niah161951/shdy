# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/19 17:25
import requests
from SHDY.public import The_random_number
from SHDY.public.conf_test import Config

dy_mch_no = Config().get_param("mercid")
dy_mch_no1 = Config().get_param("id")
order_no = The_random_number.order_number()
url = 'http://localhost:8080/DemoJava/merchantInfo/card/bal'
data ={
    "org_no": "121",
    "dy_mch_no": dy_mch_no,
    "token": "e41669b81958498182f6550a02ff13c0",
    "sign": "121212"

}

re = requests.post(url,json=data,verify=False).json()
print(re)

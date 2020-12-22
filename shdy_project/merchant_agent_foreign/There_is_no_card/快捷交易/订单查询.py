# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/10 18:57
import requests
from SHDY.public import The_random_number as a
from SHDY.public.conf_test import Config
orderNo = a.order_number()
merOrderNo = Config().get_param('merOrderNo')
dyMchNo = Config().get_param("mercid")
dyMchNo1 = Config().get_param("id")
url = 'https://116.228.47.74:7443/transaction_agent/card/qryOrder'
data = {
            "orgNo": "121",
            "dyMchNo": dyMchNo,
            "orderNo": orderNo,  #流水号
            "merOrderNo": merOrderNo,
            "qryType": "0",    #0:消费状态;1:结算状态
            "sign": "ccccccccc"
}
reg = requests.post(url,json=data).json()
print(reg)
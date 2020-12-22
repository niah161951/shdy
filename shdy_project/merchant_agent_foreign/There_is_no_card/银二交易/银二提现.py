# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/5 9:17
import requests
from SHDY.public.conf_test import Config

tradeNo = Config().get_param("mer_order_no")
dyMchNo = Config().get_param("mercid")
dyMchNo1 = Config().get_param("id")
url = 'http://localhost:8080/DemoJava/settle/mer/pay'
data = {
         "orgNumber":"121",                  #机构号
         "dyMchNo":dyMchNo,                  #电银商户号
         "amt":"449",                           #提现金额
         "fee":"1",                           #提现手续费
         "tradeNo":tradeNo,                   #交易流水号获取交易的流水单号
         "tradeDate":"20200219",              #交易日期
         "tradeTime":"174323",                #交易时间
         "token":"e41669b81958498182f6550a02ff13c0"
}
reg = requests.post(url,json=data).json()
print(reg)
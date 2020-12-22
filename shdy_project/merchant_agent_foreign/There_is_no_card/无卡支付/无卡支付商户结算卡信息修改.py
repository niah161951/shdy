# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/4 14:53
import requests
from SHDY.public import The_random_number
from SHDY.public.conf_test import Config
seqNo = The_random_number.order_number()
mercCnm = The_random_number.Company()
mercid = Config().get_param("mercid")
stlOac = The_random_number.credit_card_number()
#print(stlOac)
url  = 'http://localhost:8080/DemoJava/fastMerchant/noCardPay/updCardInfo'
data = {
          "orgNumber": "121",             #机构代码
          "mercId": mercid,            #电银商户号
          "seqNo": seqNo,          #请求流水号
          "stlOac":'6210951573972556824' ,                #银行账号借记卡
          "mercMbl": "17688888889",               #预留手机号
          "stlWcLbnkNo": "307100003019",             #联行行号
          "sign": "string"         #签名
}
reg = requests.post(url,json=data).json()
print(reg)
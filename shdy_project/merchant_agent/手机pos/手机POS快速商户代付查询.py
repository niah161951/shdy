# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/12 17:18

# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/12 15:56
import requests
from SHDY.public import   The_random_number
from SHDY.public.conf_test import Config
tradeNo = The_random_number.order_number()
tradeNo =Config().get_param('tradeNo')
mercId = Config().get_param('mercIdshouchi')
url = 'http://localhost:8080/DemoJava/settle/posMer/pay/qry'
data = {
          "mercId": mercId,    #快速商户号
          "orgNumber": "113",      #机构号
          "tradeNo": tradeNo,    #代付流水号
          "sign": "141620"
}
reg = requests.post(url,json=data,verify=False).json()
print(reg)

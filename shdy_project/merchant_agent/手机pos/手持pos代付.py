# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/12 15:56
import time
import requests
from config.configs import Config
from public.mocks import Mock

tradeNo = Mock().get_time()
tradeNo =Config().read_conf('tradeNo')
mercId = Config().get_param('mercIdshouchi')
tradeDate = time.strftime("%Y%m%d", time.localtime())

#需要修改身份证号，手机号和卡号。风控限制
url = 'http://localhost:8080/DemoJava/settle/posMer/pay'
data = {
          "fee": "2",            #代付手续费
          "mercId": mercId,    #快速商户号  DYF801000326
          "orgNumber": "113",  #机构号
          "settAmt": "6",       #代付金额
          "tradeDate": tradeDate,
          "tradeNo": tradeNo,
          "tradeTime": "124433"
}
reg = requests.post(url, json=data).json()
print(reg)

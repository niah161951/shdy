# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/12 19:00
from SHDY.public import configtest,requeststest

ip = configtest.Config().read_param('IP','cbs对账系统')
url = ip + 'checkBatch/fileGenerateZhanxin?'
data = {
          "startCheckDate": 20200726,
          "endCheckDate":20200727
}
requeststest.apitest().request_method('GET',url,data)

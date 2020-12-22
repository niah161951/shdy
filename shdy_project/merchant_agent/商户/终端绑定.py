#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/25 11:25
from SHDY.public import requeststest,configtest

ip = configtest.Config().read_conf('IP','HH代理商平台')
url = ip + 'terminal/binding'
# mercid = configtest.Config().read_conf('mercid','小微商户')
data = {
     "tsn":"V90T00000041",
     "dyTermNo":"08001342",
     "dyMchNo":'3554465465456'
}
requeststest.apitest().run_main('post',url,data)

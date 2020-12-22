#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/7/15 15:15
import requests,json
from SHDY.public import data_test,configtest

url = 'http://192.168.31.161:18380/transaction_agent/payBack/trans'
data = {

    "org_no": "121",
    "dy_mch_no": "121121172300002",
    "order_no": "20200402019111",
    "mer_order_no": '12344325',
    "service": "query",
    "sign": "YKbbEMoxz1pc2iIa5lnMot200mZs/QWozdWDBWO/o39UBFw69WUuWCD5r6dZpGPf8e4SwAo7ymgBo4wZGznNddXOxt+m3doVlgSj+BhegAADffpz0if8Yj2UYQQ68GJuNK2SOMEtBNfOfLZZOB2ADRV1mbpeelyx85t3kz6LIg4="
}
req = requests.post(url,json=data,verify=False).json()
res = json.dumps(req,indent=4,ensure_ascii=False)
print(res)
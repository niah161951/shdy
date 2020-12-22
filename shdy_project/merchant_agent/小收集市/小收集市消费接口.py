#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/7/15 11:10
import requests,json

from SHDY.public import data_test,conf_test
mer_order_no = data_test.Mock().get_time()
trans_amount = 5400  #金额（分）
url = 'https://116.228.47.74:6443/transaction_agent/payBack/trans'
data = {
        "mer_order_no": mer_order_no,
        "trade_code": "1003",
        "service": "pay",
        "org_no": "121",
        "dy_mch_no": "121121172300002",
        "pick_mer_id": "872433879990002",
        "pick_term_no": "08001492",
        "trans_amount":trans_amount,
        "trans_fee_rate":"0.038",
        "card_no": '6216261000000000018', #卡号
        "mobile": "13552535506",
        "device_id": "123456",
        "device_type": "1",
        "source_ip": "192.168.31.171",
        "account_id_hash": "CDA00f",
        "sign": "gBPK9hb90FqW2JJG5Q1njyvG91f9fEyhVPGhKvaW2PlF8l+qNZUPV4aXmMGH292WEeGX1Fx+wVX8IZ7j3tSawby/5aGJ5LHfC4gwaz6CWQZOtQNX3HAwAhTHDqIcQu1qJJ5C7h+vIvu6b+9wDgaF3hFnn+urO+Grcbsy+sgtysE="
}
res = requests.post(url,json=data,verify=False).json()
req = json.dumps(res,indent=4,sort_keys=True,ensure_ascii=False)
conf_test.Config().set_param('mer_order_no',mer_order_no)
print(req)

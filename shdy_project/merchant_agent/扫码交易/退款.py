#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/7/16 14:28

import requests,json
from SHDY.public import data_test,conf_test
mer_refund_order_no = data_test.Mock().get_time()
# mer_order_no = '20200716155729' #退款号
refund_amount = 0.01 #金额分
mer_order_no = conf_test.Config().get_param('微信外部订单号')
url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
data = {
    "body":{
    "trancde":"P02",
    "mer_order_no":mer_order_no,
    "refund_amount":refund_amount,
    "mer_refund_order_no":mer_refund_order_no
    },
    "head":{
    "trm_sn":"061310000003",
    "imei":"061310000003",
    "merc_id":"10111179990093",
    "trm_id":"08231257",
    "org_id":"101",
    "send_time":"20200716142150",
    "station_info":"460|00|6334|20504",
    "sign":"ThisIsSignPleasePressButton"
    }
}
res = requests.post(url,json=data).json()
req = json.dumps(res,indent=4,sort_keys=False,ensure_ascii=False)
print(req)

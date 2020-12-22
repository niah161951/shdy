#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/4 10:12
from SHDY.public import data_test,configtest,requeststest

'''
二维码区分是否银二或者AT
跳码区分以一下两个字段
pick_mer_id  pick_term_no
银二需配合下列地址
https://open.unionpay.com/ajweb/help/qrcodeFormPage/coverSweepReceiverApp
'''
pay_amount = 1    #金额(分)
mer_order_no = data_test.Mock().get_time()
bar_code = input('请输入微信、支付宝、银联二维码：')

url = configtest.Config().read_conf('IP','HH被扫')
data = {
    "head": {
        "merc_id": configtest.Config().read_conf('MERCID','hh快速商户'),
        "pick_mer_id": configtest.Config().read_conf('MERCID','hh池商户1'),
        "pick_term_no": configtest.Config().read_conf('terminal','hh池商户1'),
        "station_info":"116.231280,40.220770&上海市浦东新区",
        "trm_id": "08231257",
        "org_id": "101",
        "dev_typ": "3",
        "ios_typ": "IOS",
        "ios_ver": "ios9.0",
        "dev_id": "868145017549928",
        "dev_bra_nm": "iPhone",
        "dev_mod_nm": "iPhone 8s",
        "mac": "AA:BB:AA:DD:CC:FF",
        "ip_ver": "ipv4",
        "ip": "180.164.182.174",
        "is_first":"1",  # 0非首刷  1首刷  不传默认非首刷
        "sign":"jthS9NzprUMVMrZiZw7kCVv3p8RwURc+JaahhyeMK+SC/8A4V5aYU66Ln0cvmylnjPd+XjrLOLnYYYQk5JL+VDtRCAv4rmkXLI1Lx9RBpqGDhxqEwJxx5VbZhFcZXPHXXPSziB3aYS3WB+97ItHkm3904NcfBfUbN/+Uj0fsbcM=",
        # "mchFlag":"121.601768", #经纬度
        # "lonLat":"31.18486",    #经纬度
        # "address":"上海金科路",
    },
    "body": {
        "mer_order_no": mer_order_no,
        "out_order_no": "",
        "trancde": "P00",  # P00：默认值，支持微信、支付宝、云闪付 交易码
        "bar_code": bar_code,  #付款码
        "pay_amount": pay_amount, #金额
        "undiscountable_amount": "",
        "order_name": "扫码交易",
        "order_desc": ""
    }
}

if bar_code.startswith('1'):
    configtest.Config().set_param('微信外部订单号',mer_order_no)
elif bar_code.startswith('2'):
    configtest.Config().set_param('支付宝外部订单号',mer_order_no)
else:
    configtest.Config().set_param('银联二维码外部订单号',mer_order_no)
requeststest.apitest().run_main('post',url,data)

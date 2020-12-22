#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/9 17:08
import time,requests
from SHDY.public import  data_test,configtest

mer_order_no = data_test.Mock().get_time()
print(mer_order_no)
pay_type = input('请输入支付方式01 微信 02支付宝： ')
merc_id = '11610265311000a'            #商户号
org_id = '116'                         #机构号
pay_amount = '1'                       #金额（分）

url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'
date = {
        "body": {
            "trancde": "P05",
            "mer_order_no": mer_order_no,
            "pay_amount": pay_amount,
            "notify_url": "http://gggggggg.com"
        },
        "head": {
            "trm_sn": "061310000003",
            "imei": "061310000003",
            "merc_id": merc_id,
            "trm_id": "08001435",
            "org_id": org_id,
            "send_time": "20200609171347",
            "station_info": "460|00|6334|20504",
            "sign": "ThisIsSignPleasePressButton"
        }
    }
sign = requests.post(url,json=date).text

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
date = {
            "body": {
                "trancde": "P05",
                "mer_order_no": mer_order_no,
                "pay_amount": pay_amount,
                "notify_url": "http://gggggggg.com"
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20200609171347",
                "station_info": "460|00|6334|20504",
                "sign": sign
            }
        }
res = requests.post(url,json=date).json()
datas = res['body']['code_url']

dr = data_test.Driver().dr()
dr.maximize_window()
dr.get('https://cli.im/')
dr.find_element_by_id('text-content').send_keys(datas)
dr.find_element_by_id('click-create').click()
time.sleep(15)
dr.quit()
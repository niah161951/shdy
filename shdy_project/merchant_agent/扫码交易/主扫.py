#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/4 16:23
from common.api import Apitest
from public.mocks import Mock
# merc_id = configtest.Config().read_conf('MERCID','hh标准商户')

pay_amount = 1  #金额分

url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
date = {
    "head": {
        "merc_id": '101290459460002',
        "station_info":"",
        "trm_id": "08231257",
        "org_id": "101",
        "sign":"Pkb9ZbxckUGvCU6BKafhBFm5U8hM5EWqRe6Ys09SSn2LkHYZpLmcJCchNfgAT8Gi0/aweZ8peSDu2BziNrLuj5HE6dgnbIsKPXy5jjduzzHv5oqAU7aXarDdBxcDRSrKPZOpZGTG80zgHJKMkRkpjpEMHr53A/nw79pbqVkwSf4=",
        "dev_typ": "3",
        "ios_typ": "IOS",
        "ios_ver": "ios9.0",
        "dev_id": "868145017549928",
        "dev_bra_nm": "iPhone",
        "dev_mod_nm": "iPhone 8s",
        "mac": "AA:BB:AA:DD:CC:FF",
        "ip_ver": "ipv4",
        "ip": "180.164.182.174",
        "mchFlag":"121.601768",
        "lonLat":"31.18486",
        "address":"上海金科路",
        "is_first": "1"  # 0非首刷  1首刷  不传默认非首刷
        # "pick_mer_id":  pick_mer_id,
        # "pick_term_no": pick_term_no
    },
    "body": {
        "pay_amount": pay_amount,
        "trancde": "P04",  # P03 微信动态码  P04 云闪付二维码  P05 支付宝动态码
        "mer_order_no":Mock().get_time() ,
        "notify_url": "http://192.168.31.161:28380/test_agent/notify/async"
    }
}
req = Apitest().run_main('post',url,date)

# 网页 = req['body']['code_url']
# # print(网页)
#element = webui.WebuiKeys('chrome','https://cli.im/')
# element.wait(10)
# element.get_text('id',"text-content",网页)
# element.click('id','click-create')
# element.sleep(15)
# element.quit()














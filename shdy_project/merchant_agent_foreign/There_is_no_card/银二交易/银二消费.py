# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/17 10:28
import requests
from SHDY.public import data_test
from SHDY.public.conf_test import Config

mer_order_no = data_test.Mock().order_number()
dy_mch_no = Config().get_param("mercid")
dy_mch_no1 = Config().get_param("id")
Config().set_param('mer_order_no',str(mer_order_no))
url = 'https://116.228.47.74:7443/transaction_agent/payBack/trans'
data = {
    "org_no": "121",
    "dy_mch_no": dy_mch_no,
    "mer_order_no": mer_order_no,
    "trans_amount": "50000",              #单位分
    "trans_fee_rate": "0.1",           #交易手续费
    "trade_code": "1002",                #1002 – 代付支付
    "card_no": "6221558812340013",      #交易卡号
    "mobile": "13552535506",            #手机号
    "device_id": "12345678901234",      #设备标识
    "device_type": "1",                 #设备类型1:手机，2:平板，3:手表，4:PC
    "source_ip":"192.168.31.171",
    "account_id_hash":"CDA00f",         #应用提供方账户
    "service":"pay",
    "pick_mer_id":"872102358120070",    #自选商户
    "pick_term_no":"08000656",
    "sign":"121212"
}
rea = requests.post(url,json=data,verify=False).json()
print(rea)
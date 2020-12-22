# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/3/5 15:25
import requests,json
from   SHDY.public import configtest,data_test

mer_order_no = 'CO9572007261101119815921'
merc_id = '872291447890001'
org_id = '125'
#mer_order_no = conf_test.Config().get_param('mer_order_no')
# # merc_id = data_test.Data().Data_merchants()['标准商户']
# org_id = '125'
url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'
data = {
        "body": {
            "trancde": "PF0",
            "mer_order_no": mer_order_no
        },
        "head": {
            "trm_sn": "061310000003",
            "imei": "061310000003",
            "merc_id": merc_id,
            "trm_id": "08001435",
            "org_id": org_id,
            "send_time": "20200305154957",
            "station_info": "460|00|6334|20504",
            "sign": "ThisIsSignPleasePressButton"
	}
}
sign = requests.post(url,json=data).text

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
data = {
        "body": {
            "trancde": "PF0",
            "mer_order_no": mer_order_no
        },
        "head": {
            "trm_sn": "061310000003",
            "imei": "061310000003",
            "merc_id": merc_id,
            "trm_id": "08001435",
            "org_id": org_id,
            "send_time": "20200305154957",
            "station_info": "460|00|6334|20504",
            "sign": sign
	}
}

reg = requests.post(url,json=data).json()
rea = json.dumps(reg,indent=2,sort_keys=True,ensure_ascii=False)
print(rea)
#返回参数 dt_switch_flag  0-D0； 1 -D0转D1 ；2-D0转T1 ；3-T1 ；4-D1
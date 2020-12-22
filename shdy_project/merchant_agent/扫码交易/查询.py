# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/9 14:25
import requests,json
from SHDY.public import data_test, conf_test

merc_id = data_test.Data().Data_merchants()['HH小微商户']
mer_order_no = conf_test.Config().get_param('银联二维码外部订单号')

url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
date = {
        "body": {
            "trancde": "PF0",
            "mer_order_no": mer_order_no
        },
        "head": {
            "trm_sn": "061310000003",
            "imei": "061310000003",
            "merc_id": merc_id,
            "trm_id": "08001435",
            "org_id": "101",
            "send_time": "20200603150743 ",
            "station_info": "460|00|6334|20504",
            "sign": "xxxx"
        }
}
rea = requests.post(url,json=date).json()
res = json.dumps(rea,indent=4,sort_keys=True,ensure_ascii=False)
print(res)
#返回参数 dt_switch_flag  0-D0； 1 -D0转D1 ；2-D0转T1 ；3-T1 ；4-D1

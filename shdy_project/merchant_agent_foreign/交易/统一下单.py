# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2020/1/2 18:27
import requests,json
from   SHDY.public import conf_test,data_test

mer_order_no = data_test.Mock().get_card_number()
pay_type = '01'                       #支付方式  01 微信   02支付宝
merc_id = '872112378410001'            #商户号
pay_amount = '1'                       #金额（分）
conf_test.Config().set_param("mer_order_no", str(mer_order_no))

url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'
data = {
        "body": {
            "open_id": "2088002093276180",
            "pay_amount": "1",
            "currency": "CNY",
            "client_ip": "127.0.0.1",
            "order_time": "20200609172021",
            "trancde": "P10",
            "notify_url": "http://gggggggg.com",
            "mer_order_no": mer_order_no,
            "order_name": "test 1111",
            "trans_type": "WX_JSAPI" #WX_JSAPI    AL_JSAPI
        },
        "head": {
            "charset": "UTF-8",
            "merc_id": merc_id,
            "org_id": "125",
            "send_time": "20200609172021",
            "sign": "ThisIsSignPleasePressButton",
            "sign_type": "RSA",
            "version": "1.0"
        }
    }
#print(type(data))
sing = requests.post(url,json=data).text

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
data = {
        "body": {
            "open_id": "2088002093276180",
            "pay_amount": "1",
            "currency": "CNY",
            "client_ip": "127.0.0.1",
            "order_time": "20200609172021",
            "trancde": "P10",
            "notify_url": "http://gggggggg.com",
            "mer_order_no": mer_order_no,
            "order_name": "test 1111",
            "trans_type": "AL_JSAPI"
        },
        "head": {
            "charset": "UTF-8",
            "merc_id": merc_id,
            "org_id": "125",
            "send_time": "20200609172021",
            "sign": "ThisIsSignPleasePressButton",
            "sign_type": "RSA",
            "version": "1.0"
        }
    }
req = requests.post(url,json=data).json()
rea = json.dumps(req,indent=2,sort_keys=True,ensure_ascii=False)
print(rea)
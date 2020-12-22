# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2020/1/2 18:27
import requests,json
from   SHDY.public import configtest,data_test

mer_order_no = data_test.Mock().get_card_number()
print(mer_order_no)
bar_code = input('请输入二维码：')
pay_type = input('请输入支付方式01 微信 02支付宝： ')                       #支付方式
merc_id = '872112378410001'
pay_amount = '1'                       #金额（分）
configtest.Config().set_param("mer_order_no", str(mer_order_no))

url = 'http://10.1.31.33:28380/test_agent/testScan/getSign'
data = {
	"body": {
		"trancde": "P00",
		"mer_order_no": mer_order_no,
		"pay_amount": pay_amount,
		"order_name": "testName",
		"pay_type": pay_type,
		"bar_code": bar_code
	},
	"head": {
		"trm_sn": "061310000003",
		"imei": "061310000003",
		"merc_id": merc_id,
		"trm_id": "08001435",
		"org_id":  '125',
		"send_time": "20190813195059",
		"station_info": "460|00|6334|20504",
		"sign": "ThisIsSignPleasePressButton"
	}
}
sing = requests.post(url,json=data).text

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
data = {
	"body": {
		"trancde": "P00",
		"mer_order_no": mer_order_no,
		"pay_amount": pay_amount,
		"order_name": "testName",
		"pay_type": pay_type,
		"bar_code": bar_code
	},
	"head": {
		"trm_sn": "061310000003",
		"imei": "061310000003",
		"merc_id": merc_id,
		"trm_id": "08001435",
		"org_id": '125',
		"send_time": "20190813195059",
		"station_info": "460|00|6334|20504",
		"sign": sing
	}
}

req = requests.post(url,json=data).json()
rea = json.dumps(req,indent=2,sort_keys=True,ensure_ascii=False)
print(rea)
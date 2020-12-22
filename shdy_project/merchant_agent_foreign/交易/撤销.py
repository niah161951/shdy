# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生 
# 创建时间 : 2020/1/3 12:28
import requests,json
from  SHDY.public import conf_test

mer_order_no = conf_test.Config().get_param('mer_order_no')
mer_order_no = '5537984825085952'
# merc_id = '872112378410001'
merc_id = '101290459460002'
org_id = '101'
url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'

data = {
	"body": {
		"trancde": "P01",
		"mer_order_no": mer_order_no
	},
	"head": {
		"trm_sn": "061310000003",
		"imei": "061310000003",
		"merc_id": merc_id,
		"trm_id": "08001435",
		"org_id": org_id,
		"send_time": "20190813195059",
		"station_info": "460|00|6334|20504",
		"sign": "ThisIsSignPleasePressButton"
	}
}
sing = requests.post(url,json=data).text

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
data = {
	"body": {
		"trancde": "P01",
		"mer_order_no": mer_order_no
	},
	"head": {
		"trm_sn": "061310000003",
		"imei": "061310000003",
		"merc_id": merc_id,
		"trm_id": "08001435",
		"org_id": org_id,
		"send_time": "20190813195059",
		"station_info": "460|00|6334|20504",
		"sign": sing
	}
}
reg = requests.post(url,json=data).json()
rea = json.dumps(reg,indent=2,sort_keys=True)
print(rea)
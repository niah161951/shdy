# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2020/1/2 17:28
import requests
from SHDY.public import data_test,configtest

rodNo = data_test.Mock().get_time()

url = 'http://116.228.47.74:18280/merchant_agent/rest/agent/sett/req'
data = {
    "orgNo":"101",       #机构号
    "agentNo":"00005",   #代理商编号
    "amt":"1",           #提现金额
    "ordNo":rodNo        #商户订单号
}
req = requests.post(url=url,json=data).json()
sett = req['settOrdNo']
configtest.Config().set_param('settOrdNo',str(sett))
print(req)

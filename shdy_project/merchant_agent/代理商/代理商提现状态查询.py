# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2020/1/2 17:36
import requests
from SHDY.public.configtest import Config
settOrdNo = Config().set_param('settordno')

url = 'http://116.228.47.74:18280/merchant_agent/rest/agent/sett/sts/qry'
data = {
    "orgNo":"101",                  #机构号
    "agentNo":"00005",                #代理商编号
    #"ordNo":"201912010034913706",                  #商户订单号
    "settOrdNo":settOrdNo                    #提现订单号
}
req = requests.post(url=url,json=data).json()
print(req)
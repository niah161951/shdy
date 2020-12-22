# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生 
# 创建时间 : 2020/1/2 17:41
import requests
url = 'http://116.228.47.74:18280/merchant_agent/rest/agent/sett/bal/qry'
data = {
        "orgNo":"101",       #机构号
        "agentNo":"00005"         #代理商编号
}
a = requests.post(url,json=data).json()
print(a)
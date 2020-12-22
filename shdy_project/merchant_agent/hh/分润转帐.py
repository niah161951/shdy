# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生 
# 创建时间 : 2019/12/30 16:41
import requests
from SHDY.public import data_test
logNo = data_test.Mock().get_time()


url = 'http://116.228.47.74:18280/merchant_agent/rest/fractionalTransfer/req'
data = {
        'memberId':'00005',  # 代理商编号
        'orgNo':'101',       #机构号
        'txnAmts':'66',      #金额
        'logNo':logNo        #流水号
}

reg = requests.post(url=url,json=data).json()
print(reg)

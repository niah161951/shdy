# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/3/10 13:43
import requests,time
from SHDY.public import  data_test,conf_test

mercId = conf_test.Config().get_param('mercIdshouchi')
seqNo = data_test.Mock().get_time()
orgOrderId = conf_test.Config().get_param('tradeNo')
orderTime = (time.strftime("%Y%m%d", time.localtime()))+'124433'

url = 'http://192.168.31.161:28380/test_agent/tool/qian?type='
data = {
        "tranCode":"MP002",
        "seqNo":seqNo,
        "orgId":"113",
        "mercId":mercId,
        "trmNo":"08002048",
        "acqNm":"电银acqNm",
        "orderId":seqNo,        #交易订单号
        "orgOrderId":orgOrderId,#原交易订单号
        "orderTime":orderTime,   #交易时间
        "payType":"1",          #0：银行卡1：支付宝2：微信3：银联二维码
        "posEmCode":"073",
        "acqNo": "acqno",
        "uniBatNo":"000100",
        "referNo": "ReferNo",
        "uniSeqNo":"000200",
        "setDate":"20200220",
        "chaSeqNo":"ChaSeqNo",
        "baseStation":"460|0|21681|14801",
        "sign":""
}
sign = requests.post(url,json=data,verify=False).text
#print(a)

url = 'http://192.168.31.161:18380/transaction_agent/tel/pos'
data = {
        "tranCode":"MP002",
        "seqNo":seqNo,
        "orgId":"113",
        "mercId":mercId,
        "trmNo":"08002048",
        "acqNm":"电银acqNm",
        "orderId":seqNo,         #交易订单号
        "orgOrderId":orgOrderId, #原交易订单号
        "orderTime":orderTime,    #交易时间
        "payType":"1",           #0：银行卡1：支付宝2：微信3：银联二维码
        "posEmCode":"073",
        "acqNo":"acqno",
        "uniBatNo":"000100",
        "referNo":"ReferNo",
        "uniSeqNo":"000200",
        "setDate":"20200220",
        "chaSeqNo":"ChaSeqNo",
        "baseStation":"460|0|21681|14801",
        "sign":sign
}

b = requests.post(url,json=data,verify=False).json()
print(b)
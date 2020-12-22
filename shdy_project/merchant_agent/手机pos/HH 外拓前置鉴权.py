# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/2/25 10:36
import requests
from config.configs import Config

seqNo = Config()

url = 'http://localhost:8080/DemoJava/fourAuth/check'
data = {
         "orgNumber":"113",
         "seqNo":seqNo,
         "authType":"3",   #2 - 二要素3 - 三要素4 - 四要素
         "parType":"3NIC",  #2NI - 二要素（姓名+身份证）3NIC - 三要素（姓名+身份证+卡号）3NIM - 三要素（姓名+身份证+手机号）4NICM - 四要素（姓名+身份证+卡号+手机号）
         "reqCnl":"FROYF",
         "txnTyp":"2",    #1 - 注册2 - 交易3 - 结算4 - 出款5 - 变更
         "authObj":"1",   #1 - 法人2 - 交易人3 - 结算人
         "idNm":"杨迪",  #2      3   4
         "idNo":"420113199407210015", #证件号码2 3  4
         "idType":"00",   #00 – 身份证
         "bankNo":"6225809448285669",#卡号  3 4
         "mobile":"13697120534",#手机号          4
         "mercId":"",    #商户号
         "mercNm":"",    #商户名
         "eqType":"",#1 - 传统pos2 - 智能pos3 - 手机
         "eqId":"",#设备唯一标识
         "ipAdr":""
}
a = requests.post(url,json=data,verify=False).json()
print(a)
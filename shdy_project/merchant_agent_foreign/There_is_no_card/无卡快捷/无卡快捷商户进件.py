# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/4 15:37

import requests
from SHDY.public import data_test
from SHDY.public.configtest import Config

seqNo = data_test.Mock().get_time()
mercCnm = data_test.Mock().get_Company()

url = 'http://192.168.20.171:18880/DemoJava/fastMerchant/inComing'
data = {
     "orgNumber":"121",                  #机构代码
     "outMercId":"2165464446468",                     #外部商户号
     "seqNo":seqNo,                         #请求流水号
     "mercMbl":"13552535506",                       #商户手机号
     "mercCnm":mercCnm,                       #商户名称
     "mercAbbr":"商户",                      #商户简称
     "mccCd":"5812",                     #MCC码
     "mercProv":"2900",                  #归属省
     "mercCity":"2904",                  #归属市
     "mercCounty":"2904",                #归属县区
     "busAddr":"北京小卖部",                       #营业地址
     "crpIdTyp":"0",                     #法人证件类型
     "crpIdNo":"341126197709218366",                       #法人证件号码
     "crpNm":"全渠道",                         #法人姓名
     "crpExpDtD":"20991010",                     #法人证件过期日期
     "stlSign":"1",                              #结算账号公私标志
     "stlWcLbnkNo":"308651020015",                   #联行行号
     "stlOac":'5200831111111113',                      #银行账号贷记卡
     "bnkAcnm":"全渠道",                            #银行开户名称
     "usrOprEmail":"123@qq.com",                   #商户管理员EMAIL
     "debitFee":"0.0038",                      #快捷借记费率
     "debitFeeLimit":"30",                     #借记封顶额
     "creditFee":"0.0038",                     #快捷贷记费率
     "d0Fee":"0.0038",                         #D0额外手续费费率
     "d0FeeQuota":"1"                          #D0额外定额手续费
}

reg = requests.post(url,json=data).json()

Config().set_param("id",reg['mercId'])
print(reg)


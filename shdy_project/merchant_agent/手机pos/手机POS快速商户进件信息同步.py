# -*- coding: utf-8 -*-
# 作者  : 一蓑烟雨任平生
# 时间  : 2020/1/6 13:59
import requests
from config.configs import Config
from public.mocks import Mock

seqNo = Mock().get_card_number()
phon = Mock().get_phone()
mercCnm = Mock().get_name()
busAddr = Mock().get_address()
crpIdNo = Mock().Id_card()
crpNm = Mock().get_name()
usrOprEmail = Mock().email()
mercId = Mock().credit_card_number()

#print(mercid)
url = 'http://localhost:8080/DemoJava/fastMerchant/pos/inComing'
data = {
        'orgNumber': '113',  # 机构代码
        'mercId': mercId,  # 快速商户号
        # 'mercId': '4468165499760',  # 快速商户号手动输入
        'synType': '0',  # 同步类型 0-新增 1-修改
        'seqNo': seqNo,  # 请求流水号
        'mercMbl': phon,  # 商户手机号
        # 'mercMbl': '13818765279',  # 商户手机号
        'mercCnm': mercCnm,  # 商户名称
        'mercAbbr': mercCnm,  # 商户简称
        # 'mercCnm': '杰',  # 商户名称
        # 'mercAbbr': '杰',  # 商户简称
        'mccCd': '7999',  # MCC码
        'mercProv': '1000',  # 归属省
        'mercCity': '1000',  # 归属市
        'mercCounty': '1034',  # 归属县区
        'busAddr': '上海浦东小卖部',  # 营业地址
        'crpIdTyp': '0',  # 法人证件类型0-身份证
        'crpIdNo': crpIdNo,  # 法人证件号码
        'crpNm': crpNm,  # 法人姓名
        # 'crpIdNo': '445302195403137924',  # 法人证件号码
        # 'crpNm': '涛',  # 法人姓名
        'crpExpDtD': '20991230',  # 法人证件过期日期   1
        'stlSign': '1',  # 结算账号公私标志1 对私
        'stlWcLbnkNo': '102110010037',  # 联行行号    1
        'stlOac': '6225804796885153',  # 银行账号  1
        'bnkAcnm': crpNm,  # 银行开户名称
        'usrOprEmail':usrOprEmail   # 商户管理员EMAIL
        # 'bnkAcnm': '涛',  # 银行开户名称
        # 'usrOprEmail':'xugang@yahoo.com'   # 商户管理员EMAIL
        #'sign': '221'  # 签名
}
reg = requests.post(url,json=data).json()
Config().set_param('mercIdshouchi',str(reg['mercId']))
print(reg)
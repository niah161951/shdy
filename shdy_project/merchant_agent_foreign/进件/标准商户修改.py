# -*- coding: utf-8 -*-
from SHDY.public.configtest import Config
from SHDY.public.data_test import Mock
from SHDY.public import requeststest

mercId = Config().read_conf("MERCID","标准商户")
ip = Config().read_conf('IP','华为云标准版代理商平台')
url = ip + 'standardMerchant/update'
data = {
        'orgNumber': '105',  # 机构代码
        'seqNo': Mock().get_time(),  # 流水号
        'updType': '1',  # 类型  1基本   2结算   3费率   5 协议补充
        'mercId': '872121155920019',  # 电银商户号
        'mchStatus': '0',  # 商户状态0：正常 1：关闭
        'settStatus': '0',  # 商户结算状态  0 – 正常 1 – 关闭
        'mercMbl': '17653288603',  # 商户手机号   1
        # 'mercCnm': '大地李初',  # 商户名称     1
        'mercAbbr': Mock().get_Company(),  # 商户简称    1
        'stlSign': '0',  # 结算账号公私标志  0：对公 1：对私   2
        'stlWcLbnkNo': '309290000480',  # 联行行号                       2
        'stlOac': '216490100100122275',  # 银行账号                           2
        'bnkAcnm': '忆洋',  # 银行开户名称                      2
        'debitFee': '0.005',  # 借记费率
        'debitFeeLimit': '25',  # 借记封顶额
        'creditFee': '0.005',  # 贷记费率
        'd0Fee': '0.0055',  # D0额外手续费费率
        'd0FeeQuota': '',  # D0额外定额手续费
        'unionCreditFee': '0.005',  # 云闪付贷记费率
        'unionDebitFee': '0.005',  # 云闪付借记费率
        'aliFee': '0.005',  # 支付宝费率
        'wxFee': '0.005',  # 微信费率
        'sign': '0',  # 签名
        'BGSQD': '',  # 变更申请单
        'JSZHZM': '',  # 结算账户证明
        'JSWTS': '',  # 结算委托书
        'YHK': '',  # 银行卡正面
        'SQGXZM': '',  # 授权人关系证明
        'JBSFZ1': '',  # 经办人身份证正面
        'JBSFZ2': '',  # 经办人身份证反面
        'JSSFZ1': '',  # 结算人身份证正面
        'JSSFZ2': '',  # 结算人身份证反面
        'SCZP': '',  # 手持身份证照片
        'QT1': '',  # 其他1
        'QT2': '',  # 其他2
        'QYXY': ''  # 签约协议
}
requeststest.apitest().run_main('post',url,data)

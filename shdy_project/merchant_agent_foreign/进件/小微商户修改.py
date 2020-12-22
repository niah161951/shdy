# -*- coding: utf-8 -*-
from SHDY.public.configtest import Config
from SHDY.public.data_test import Mock
from SHDY.public import requeststest

mercId = Config().read_conf("MERCID","小微商户")

ip = Config().read_conf('IP','uat外拓项目')
url = ip + 'microMerchant/update'
data = {
        'orgNumber': '116',  # 机构代码
        'seqNo': Mock().get_time(),  # 请求流水号
        'updType': '2',  # 类型  1基本  2结算  3费率
        'mercId': '116491258140007',  # 电银商户号
        'mercMbl': '17690151611',  # 商户手机号  1
        'mercAbbr': Mock().get_Company(),  # 商户简称    1
        'busAddr': '上海市浦东新区',  # 营业地址    1
        'stlWcLbnkNo': '310290098625',  # 联行行号     2
        'stlOac': '6217920175986368',  # 银行账号     2
        'bnkAcnm': '测试二',  # 银行开户名称 2
        'debitFee': '0.005',  # 借记费率        3
        'debitFeeLimit': '25',  # 借记封顶额      3
        'creditFee': '0.005',  # 贷记费率        3
        'd0Fee': '0.005',  # D0额外手续费费率3
        'd0FeeQuota': '0.005',  # D0额外定额手续费3
        'unionCreditFee': '0.005',  # 云闪付贷记费率  3
        'unionDebitFee': '0.005',  # 云闪付借记费率  3
        'aliFee': '0.005',  # 支付宝费率      3
        'wxFee': '0.005',  # 微信费率        3
        'sign': '0'  # 签名

}
requeststest.apitest().run_main('post',url,data)


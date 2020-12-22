# -*- coding: utf-8 -*-
from SHDY.public import data_test,configtest,requeststest

ip = configtest.Config().read_conf('IP','HH代理商平台')
# 网页 = ip + 'FastMerchantIncoming/Incoming'
url = ip + 'custom/microMerchant/inComing'
data = {
          "orgNumber": "101",#机构代码
          "agentNumber": "101",#代理商代码
          "regionNo": "1034",#地区码
          "regionNoCity": "1000",#地区码市
          "regionNoProv": "1000",#地区码省
          "seqNo": data_test.Mock().get_time(),#请求流水号
          "mercId":"",   #商户ID
          "mercMbl": "13119188213",#商户手机号
          "mercCnm": data_test.Mock().get_name(),#商户名称
          "mercAbbr": data_test.Mock().get_Company(),#商户简称
          "mccCd": "8111",#MCC码
          "mercAttr": "0",#商户性质
          "crpIdTyp": "0",#0-身份证 1-护照 2-军官证
          "crpIdNo": data_test.Mock().get_card(),#法人证件号码
          "crpNm": "小西湖",#法人姓名
          "crpExpDtD": "20991231",#法人证件过期日期
          "stlSign": "1",#0 对公，1 对私
          "mercStlFlg": "1",#0 实时，1非实时
          "bankNm": "ABC",#银行名称
          "opnBnkProv": "01",#支行归属省份
          "opnBnkCity": "100",  # 支行归属地市
          "stlWcLbnkNo": "307100003019",#联行行号
          "stlOpnBnkDesc": "平安银行股份有限公司北京分行",#结算银行名称
          "stlOac": "6230580000127353865",#银行账号
          "bnkAcnm": "小西湖",#银行开户名称
          "expDtD": "20200915",#协议到期日
          "usrOprNm": "小西湖",#商户管理员姓名
          "usrOprEmail": "12312@163.com",#商户管理员EMAIL
          "debitFee": "0.005",#借记费率
          "debitFeeLimit": "26",#借记封顶额
          "creditFee": "0.0058",#贷记费率
          "creditFeeLimit": "99999999",#贷记封顶额
          "t1FeeRate": "0.00003",#T1费率
          "d0Fee": "0",#D0额外手续费费率
          "d0FeeQuota": "0",#D0额外定额手续费
          "d0StlBegAmt": "100",#D0起始结算金额
          "unionCreditFee": "0.0038",#银联二维码贷记费率
          "unionDebitFee": "0.0055",#银联二维码
          "cloudCreditFee": "0.0038",#云闪付贷记费率
          "cloudDebitFee": "0.0038",#云闪付借记费率
          "limitCreditFee": "0.0056",#小额双免贷记费率
          "limitDebitFee": "0.0055",#小额双免借记费率
          "unionFlg": "0",#是否开通云闪付 此处是扫码 0 开通，1不开通
          "outMercId": "9991031234567896",#外部商户号
          "settType": "T1",#结算类型
          "mercType": "TRADPOS",#枚举值 TRADPOS-传统POS   MPOS-小POS   INTEPOS-智能POS
          "mercLvl": "B"#商户等级  A：标准商户B：商户代理进件（快速商户）C：商户自助进件（快速商户）
}

requeststest.apitest().run_main('post',url,data)


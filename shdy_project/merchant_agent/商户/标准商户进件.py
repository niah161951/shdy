#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/22 17:05
from SHDY.public import requeststest,configtest
from SHDY.public.data_test import Mock

ip = configtest.Config().read_conf('IP','HH代理商平台')
url = ip + 'StandardMerchantIncoming/Incoming'

data = {
    "seqNo": Mock().get_time(),
    "mercCnm": Mock().get_Company(),
    "mercAttr": "1",  # 商户类型1 – 标准商户（个体）9- 其他（企业）
    "stlSign": "1",  # 结算账号公私标志，0:对公，1:对私
    # "entAccBnkNm": "平安银行",  # 企账户银行名称（商户性质为其他且结算账号公私标志为对私必传）
    # "entAccNm": "test",  # 企业账户名称（商户性质为其他且结算账号公私标志为对私必传）
    # "entAccNo": "6232068300166338200",  # 企业账号（商户性质为其他且结算账号公私标志为对私必传）
    "mercAbbr":"shanghaizhangj",
    "crpExpDtD":"20990222",
    "orgNumber":"101",
    "agentNumber":"00181",
    "expDtD":"20210427",
    "usrOprNm":"测试",
    "usrOprEmail":"lllll@111.com",
    "outMercId":"11111111122233",
    "mercProv":"2900",
    "mercCity":"2900",
    "mercCounty":"2904",
    "crpIdTyp":"0",
    "settType":"T1",

    "crpIdNo":"360101198501010013",
    "crpNm":"测试",
    "regionNo":"111",
	"bens":[
        {
            "benCertExpDt":"2030-01-01",
            "benCertNo":"330281198310054912",
            "benCertTyp":"0",
            "benDdr":"上海市松江区泗泾镇娱乐广场",
            "benNm":"李明月"
        } ],
    "busAddr":"上海市松江区泗泾镇娱乐广场",

    "mccCd":"7999",
    "mercHotLin":"021-51693317",
    "mercLvl":"A",
    "mercMbl":"13119554119",
    "mercOprMbl":"13111111111",
    "mercStlFlg":"1",
    "mgtScp":"上海市",
    "nextStlDtD":"2099-02-22",
    "opnBusDtD":"20990222",
    "regAddr":"上海市松江区泗泾镇娱乐广场",
    "regCapAmt":"10",
    "regExpDtD":"2099-02-22",
    "regId":"564SD64DSDFT",
    "stlEffDtD":"2019-10-01",
    "stlExpDtD":"2099-02-22",
    "bankNm":"ABC",
    "stlOac":"6232068300166338245",
    "bnkAcnm":"测试",
    "stlWcLbnkNo":"102290071634",
    "opnBnkProv":"04",
    "opnBnkCity":"350",
    "stlOpnBnkDesc":"平安银行股份有限公司北京分行",
    "aliFlg":"0",
    "aliItem":"123",
    "wxFlg":"0",
    "wxItem":"123",
    "unionFlg":"0",
    "debitFee":"0.006",
    "debitFeeLimit":"201",
    "creditFee":"0.006",
    "creditFeeLimit":"20000",
    "d0Fee":"0.003",
    "d0StlBegAmt":"0",
    "t1FeeRate":"0.003",
    "unionCreditFee":"0.0056",
    "unionDebitFee":"0.0055",
    "cloudDebitFee":"0.006",
    "cloudCreditFee":"0.0061",
    "limitDebitFee":"0.0059",
    "limitCreditFee":"0.0060",
    "aliFee":"0.0039",
    "wxFee":"0.0038",
    "d0FeeQuota":"1",
    "zipFilePath":"data2/upload/20190819/215839200669466624.zip"
}
requeststest.apitest().run_main('post',url,data)

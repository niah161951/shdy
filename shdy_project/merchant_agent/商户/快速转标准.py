# _*_ coding: utf-8 _*_
import requests,json
from SHDY.public.data_test import Mock
from SHDY.public.conf_test import Config

url = 'http://116.228.47.74:18280/merchant_agent/rest/StandardMerchantIncomingApend/IncomingApend'
data = {
    "seqNo":  Mock().get_time(),
    "mercId": Config().get_param("mercid"),
    "mercCnm": Mock().get_Company(),
    "mercAbbr": Mock().get_Company(),
    "crpExpDtD":"20591010",
    "bens": [
        {
            "benCertExpDt": "20191008",
            "benCertNo": "330281198310054912",
            "benCertTyp": "0",
            "benDdr": "上海市松江区泗泾镇娱乐广场",
            "benNm": "李明月"
        }
    ],
    "busAddr": "上海市松江区泗泾镇娱乐广场",
    "mercAttr": "1",
    "mccCd":"7999",  #MCC码
    "mercHotLin": "021-51693317",
    "mercLvl": "A",
    "mercMbl": "13119554119",
    "mercOprMbl": "13119554119",
    "mercStlFlg": "1",
    "mgtScp": "上海市",
    "nextStlDtD": "20191012",
    "opnBusDtD": "20191012",
    "regAddr": "上海市松江区泗泾镇娱乐广场",
    "regCapAmt": "10",
    "regExpDtD": "20250504",
    "regId": "564SD64DSDFT",
    "stlEffDtD": "20191001",
    "stlExpDtD": "20250504",
    "stlOpnBnkDesc": "平安银行股份有限公司北京分行",
    "stlSign": "1",
    "aliFee": "0.0054",
    "aliFlg": "0",
    "aliItem": "XXX",
    "wxFee": "0.0053",
    "wxFlg": "0",
    "wxItem": "XXX",
    "zipFilePath": "data2/upload/20190819/215839200669466624.zip"
}
try:
    reg = requests.post(url=url,json=data).json()
    res = json.dumps(reg,indent=2,sort_keys=True,ensure_ascii=False)
    print(res)
except Exception as error:
    print('未知错误%s'%error)
# -*- coding: utf-8 -*-
from SHDY.public import requeststest,configtest
from SHDY.public.data_test import Mock

mercid = configtest.Config().read_conf("mercId",'小微商户')
# ip = configtest.Config().read_conf('IP','HH代理商平台')
# 网页 = ip + 'microMerAppend/inComing'
ip = configtest.Config().read_conf('IP','HH代理商平台')
url = ip + 'microMerAppend/inComing'
data = {
        'seqNo':Mock().get_time(),	#请求流水号
        'mercId': mercid,	#电银商户ID
        'mercCnm':Mock().get_Company(),	#商户名称
        'mercAbbr':Mock().get_Company(),        	#商户简称
        'crpExpDtD':'20991020',    	#法人证件过期日期
        'busAddr':'上海浦东小卖部',	#营业地址
        'aliFee':'0.0038',          	#支付宝费率
        'wxFee':'0.0038',           	#微信费率
        'aliFlg':'1',          	#是否开通支付宝 0 开通，1 不开通　
        'aliItem':'0',         	#支付宝类目
        'wxFlg':'1',           	#是否开通微信 0 开通，1 不开通　
        'wxItem':'0',         	#微信类目
        'mccCd':'5331',           	#MCC码
        'zipFilePath':'data2/upload/20190730/208605112376098816.zip'	#附件名
    }
requeststest.apitest().run_main('post',url,data)

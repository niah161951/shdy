#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 17:44
from common.ui import *
from configs.conf import *

def refund(MercId,orderId):
    dr = WebuiKeys('chrome',Config().read_conf('IP','华为云jboss'))
    dr.clear('id','MercId')
    dr.send_keys('id','MercId',MercId)
    dr.clear('id','MerchantCertPass')
    dr.send_keys('id','MerchantCertPass',Config().read_conf('password','uat'))
    dr.click('xpath',
             '//html/body/center/form/table/tbody/tr[4]/td/input')
    '''统一退款demo'''
    dr.click('xpath','/html/body/center/form/table/tbody/tr[37]/td/a')
    dr.clear('id','orderId')
    dr.send_keys('id','orderId',orderId)
    dr.clear('xpath',
             '/html/body/form/center/table/tbody/tr[10]/td[2]/input')
    Order_Number = dr.get_attribute('xpath',
                                    '//*[@id="form1"]/center/table/tbody/tr[1]/td[2]/input',
                                    'value')
    Config().set_param('退款请求号',Order_Number)
    dr.click('id','Submit')
    dr.sleep(1)
    dr.click('id','Submit')
    text = dr.get_text('xpath','//html/body/pre')
    returnMessage = Config().get_str(text, 'returnMessage=', '&version')
    status = Config().get_str(text, 'status=', '&')
    if returnMessage in '交易成功' and status in 'P':
        dr.sleep(0.5)
        Log().info('退款成功')
        dr.quit()
    else:
        Log().error(f'退款失败：{status}')
        dr.quit()

if __name__=="__main__":
    # 常规交易 - 云闪付：商户号为                   872290065135002
    # 常规交易 - B2B收银台、H5收银台：商户号为       872290049000101
    # 其他常规交易：商户号为                        872290049005004
    mercid = {
        Config().read_conf('MERCID', '华为云新'):Config().read_conf('DATA', '纯聚合支付宝扫码'),
    }
    for k,v in mercid.items():
            refund(k,v)



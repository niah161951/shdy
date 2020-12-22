#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 17:46
from common.ui import *
from configs.conf import *


def alpay():
    dr = WebuiKeys('chrome',Config().read_conf('IP','华为云jboss'))
    dr.wait(10)
    dr.clear('id','MercId')
    dr.send_keys('id', 'MercId', Config().read_conf('MERCID', '华为云新'))
    dr.clear('id','MerchantCertPass')
    dr.send_keys('id','MerchantCertPass',Config().read_conf('password','uat'))
    dr.click('xpath','//html/body/center/form/table/tbody/tr[4]/td/input')
    dr.click('xpath','//html/body/center/form/table/tbody/tr[11]/td/a')
    dr.sleep(0.5)
    dr.get_select('xpath',
                  '/html/body/form/center/table/tbody/tr[2]/td[2]/select',
                  'text','支付宝扫码')
    orderId = dr.get_attribute('xpath',
                               '/html/body/form/center/table/tbody/tr[3]/td[2]/input',
                               'value')
    Config().set_param( "纯聚合支付宝扫码", orderId)
    # 不分账0 分账1
    # dr.get_select('xpath','/html/body/form/center/table/tbody/tr[16]/td[2]/select',
    #               'value','0')
    '''提交'''
    dr.click('id','Submit')
    payInfo = dr.get_text('xpath','//html/body/pre')
    returnMessage = Config().get_str(payInfo, 'rspMessage=', '&payInfo')
    rspCode = Config().get_str(payInfo, 'rspCode=', '&')
    if returnMessage in 'SUCCESS' and  rspCode in '000000' :
        payInfo = Config().get_str(payInfo, "payInfo=", "&")
        Log().info('交易成功')
        dr.sleep(0.5)
        dr.get_handle()
        url = Config().read_conf('IP', '草料')
        dr = WebuiKeys('chrome', url)
        dr.send_keys('id', 'text-content', payInfo)
        dr.click('id', 'click-create')
        dr.get_screenshots('纯聚合支付宝扫码')
    else:
        Log().error(f'交易失败: {returnMessage}')
        dr.quit()

if __name__ == '__main__':
    alpay()
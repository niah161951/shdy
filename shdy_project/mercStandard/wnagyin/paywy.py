#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 13:31
from common.ui import *
from configs.conf import *


def biaozhun():
    url = Config().read_conf('IP', '华为云jboss')
    dr = WebuiKeys('chrome', url)
    dr.wait(10)
    dr.clear('id', 'MercId')
    dr.send_keys('id', 'MercId', Config().read_conf('MERCID', '华为云新'))
    dr.clear('id', 'MerchantCertPass')
    dr.send_keys('id', 'MerchantCertPass', Config().read_conf('password', 'uat'))
    dr.click('xpath', '//html/body/center/form/table/tbody/tr[4]/td/input')
    #标准支付接口
    dr.click('xpath', '/html/body/center/form/table/tbody/tr[47]/td/a')
    dr.sleep(1)
    dr.clear('xpath','/html/body/form/center/table/tbody/tr[6]/td[2]/input')
    dr.send_keys('xpath','/html/body/form/center/table/tbody/tr[6]/td[2]/input',1)
    # #内部订单号
    # oracid = dr.get_attribute('xpath','/html/body/form/center/table/tbody/tr[4]/td[2]/input','value')
    # Config().set_param('标准个人网银',oracid)
    dr.click('id','Submit')
    #企业网银
    dr.sleep(1)
    dr.click('xpath','/html/body/jspfile/div[5]/div[2]/div/div[1]/ul/li[2]/a')
    #商户内部订单号
    orderId = dr.get_text('id','orderId')
    Config().set_param('商户内部订单号',orderId)
    dr.click('xpath','//*[@id="personalPayment"]/li[1]/img')
    dr.sleep(1)
    dr.click('xpath','//*[@id="personalPayment"]/li[1]/div/a')
    dr.quit()

if __name__ == '__main__':
    biaozhun()

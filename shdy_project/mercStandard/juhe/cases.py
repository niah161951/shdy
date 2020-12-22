#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/6 17:57
import pytest,re
import allure
from common.ui import *
from configs.conf import *


@allure.feature('pay')
class Test_case:
    url = Config().read_conf('IP', 'uat')
    urls = Config().read_conf('IP', '草料')
    def setup(self):
        print('>-----<'*10)

    def teardown(self):
        self.dr.quit()
        print('<----->'*10 )

    # @pytest.fixture()
    def login(self):
        '''
        登录支付
        :return:
        '''
        mercid = Config().read_conf('MERCID', '商户')
        password = Config().read_conf('password', 'uat')
        self.dr = WebuiKeys('chrome', self.url)
        self.dr.wait(10)
        self.dr.clear('id', 'MercId')
        self.dr.send_keys('id', 'MercId', mercid)
        self.dr.clear('id', 'MerchantCertPass')
        self.dr.send_keys('id', 'MerchantCertPass', password)
        self.dr.click('xpath', '//html/body/center/form/table/tbody/tr[4]/td/input')
        self.dr.click('xpath', '//html/body/center/form/table/tbody/tr[11]/td/a')
        self.dr.sleep(1)

    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    def test_a(self):
        self.login()
        self.dr.sleep(2)
        self.dr.get_select('xpath',
                      '/html/body/form/center/table/tbody/tr[2]/td[2]/select',
                      'text', '支付宝扫码')
        orderId = self.dr.get_attribute('xpath',
                                   '/html/body/form/center/table/tbody/tr[3]/td[2]/input',
                                   'value')
        Config().set_param("纯聚合支付宝扫码商户订单号", orderId)
        '''提交'''
        self.dr.click('id', 'Submit')
        payInfo = self.dr.get_text('xpath', '//html/body/pre')
        self.dr.sleep(1)
        payInfo = Config().get_str(payInfo, "payInfo=", "&")
        Config().set_param('支付宝扫码',payInfo)

    @allure.title("用例标题1")
    def test_b(self):
        '''
        微信公众号支付
        :return:
        '''
        self.login()
        self.dr.sleep(2)
        self.dr.get_select('xpath',
                      '/html/body/form/center/table/tbody/tr[2]/td[2]/select',
                      'text', '微信公众号')
        orderId = self.dr.get_attribute('xpath',
                                   '/html/body/form/center/table/tbody/tr[3]/td[2]/input',
                                   'value')
        Config().set_param("纯聚合微信公众号商户订单号", orderId)
        openId = Config().read_conf('Other','openid')
        self.dr.send_keys('xpath','/html/body/form/center/table/tbody/tr[4]/td[2]/input',openId)
        self.dr.click('xpath','//*[@id="Submit"]')
        text = self.dr.get_text('xpath','//html/body/pre')
        self.dr.sleep(1)
        wcPayData = Config().get_str(text,'{"', '"}')
        get_empty = re.compile('":"')
        get_etc = get_empty.sub('=', wcPayData)
        get_take = re.compile('","')
        get_replace = get_take.sub('&', get_etc)
        Joining_together = Config().read_conf('IP','拼接') + get_replace
        Config().set_param('微信公众号',Joining_together)

    @allure.title("用例标题2")
    def test_c(self):
        '''
        微信支付
        :return:
        '''
        self.login()
        self.dr.sleep(2)
        self.dr.get_select('xpath',
                      '/html/body/form/center/table/tbody/tr[2]/td[2]/select',
                      'text', '微信扫码')
        orderId = self.dr.get_attribute('xpath',
                                   '/html/body/form/center/table/tbody/tr[3]/td[2]/input',
                                   'value')
        Config().set_param("微信扫码商户订单号", orderId)
        openId = Config().read_conf('Other', 'openid')
        self.dr.send_keys('xpath', '/html/body/form/center/table/tbody/tr[4]/td[2]/input', openId)
        self.dr.click('id','Submit')
        payInfo = self.dr.get_text('xpath','//html/body/pre')
        payInfo = Config().get_str(payInfo, "payInfo=", "&")
        self.dr.sleep(1)
        Config().set_param('微信扫码',payInfo)

    @allure.title("用例标题3")
    def test_d(self):
        al = Config().read_conf('DATA','支付宝扫码')
        wx = Config().read_conf('DATA','微信扫码')
        wxg = Config().read_conf('DATA','微信公众号')
        payinfo = [al,wx,wxg]
        for  i in payinfo:
            dr = WebuiKeys('chrome',self.urls)
            dr.send_keys('id','text-content',i)
            dr.click('id','click-create')
            dr.get_screenshots('扫码')
            # dr.quit()


if __name__=='__main__':
    pytest.main('-v -s cases.py')
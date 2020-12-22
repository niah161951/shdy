#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:17
import pytest
import allure
from common.api import Apitest
from common.ui import WebuiKeys
from test_data.datas import *

@allure.feature('bangka')
class Test_case:
    url = Data().url
    htmlpath = r'D:\PycharmProject\shdy\test_data\card.html'
    def setup(self):
        print('>-----<'*10)
    def teardown(self):
        print('<----->'*10 )

    @pytest.mark.run(order=1)
    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    def test_a(self):
        data = Data().bangka()
        req = Apitest().post_main(self.url+'card/createHTML',data)
        assert req.status_code == 200
        try:
            unionPayHtml = req.text
            with open(self.htmlpath, 'w') as fb:
                fb.write(str(unionPayHtml))
            return unionPayHtml
        except Exception as  e:
            Log().error(f'异常原因{e}')

    @pytest.mark.run(order=2)
    @allure.title("用例标题1")
    @allure.story("这里是第二个二级标签")
    def test_b(self):
        self.dr = WebuiKeys('chrome', self.htmlpath)
        self.dr.wait(10)
        self.dr.send_keys('id','smsCode','111111')
        self.dr.click('id','isCheckAgreement')
        self.dr.send_keys('id','expireMonth','11')
        self.dr.sleep(1)
        self.dr.send_keys('id','expireYear','23')
        self.dr.click('id','btnCardPay')
        self.dr.click('id','isCQPAgreementChecked')
        self.dr.click('id','btnCardPay')
        self.dr.sleep(5)
        self.dr.quit()

if __name__=='__main__':
    pytest.main(['-v','-s', 'test_one.py','--maxfail=1'])
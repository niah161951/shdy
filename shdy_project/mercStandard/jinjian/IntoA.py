# -*- coding: utf-8 -*-
# @Author  : 一蓑烟雨任平生
# @Time    : 2020/12/16 9:18
from common.ui import *
from configs.conf import *
from public.mocks import Mock


def int_a():
    url = Config().read_conf('IP','华为云jboss')
    dr = WebuiKeys('chrome',url)
    dr.wait(10)
    dr.click('xpath','/html/body/center/form/table/tbody/tr[4]/td/input')
    dr.click('xpath','/html/body/center/form/table/tbody/tr[66]/td/a')
    requestId = dr.get_attribute('xpath',
                     '//*[@id="form1"]/center/table/tbody/tr[7]/td[2]/input',
                     'value')
    Config().set_param( "商户请求号", requestId)
    dr.clear('xpath','//*[@id="form1"]/center/table/tbody/tr[8]/td[2]/input')
    mercCnm = Mock().get_Company()
    dr.send_keys('xpath','//*[@id="form1"]/center/table/tbody/tr[8]/td[2]/input',mercCnm)
    Config().set_param("商户名称", mercCnm)
    dr.click('id','button2')
    dr.quit()
if __name__ == '__main__':
    int_a()
# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/10 17:31
import requests,json
from SHDY.public import data_test as a
from SHDY.public.conf_test import Config
from selenium import webdriver
from time import sleep

dyMchNo = Config().get_param("mercid")
dyMchNo1 = Config().get_param("id")
orderNo = a.Mock().get_time()
card = '6221558812340000'  #贷记卡
name = '互联网'              #姓名
id_card = '341126197709218366'            #身份证
phon ='13552535506'               #手机号
cvn2 = '123'              #信用卡
time1 = '202311'              #时间
code = '111111'                #短信验证码
url = 'https://116.228.47.74:7443/transaction_agent/card/order'
data = {
        "orgNo": "121",         #机构号
        "dyMchNo": dyMchNo1,     #商户号
        "orderNo": orderNo,     #流水号
        "transAmount": "100",     #交易金额
        "tradeCode": "10001",    #快捷支付
        "orderName": "月饼",
        "orderDesc": "中秋吃月饼",
        "frontUrl": "baid.com",
        "syncNotifyUrl": "http://192.168.31.161:28380/test_agent/notify/async",  #异步通知地址
        "sign": 'VM5izZS5ZLFKTm2vcwpXKsGl5BREkn2WPGinMnoHHM/2OqAWDtUFXWaKiR6S90mImfpQBjEO+ReU03pT0wZib6nxuZRggMOKM+Tyaso4pm3/7QwS7OSGUF5oI1NsxZZsC7+/n0CykoucEomQK+7a+u84E1pGxomTJXmmIh6swhY='
}
re = requests.post(url,json=data,verify=False).json()
ra = json.dumps(re,indent=2,sort_keys=True)
orderNo1 = re['result']['orderNo']
platNo = re['result']['platNo']
url1 = re['result']['网页']
orgNo = 'orgNo'+'='+'121'
orderNo2='orderNo'+'='+orderNo1
platNo1 = 'platNo'+'='+platNo
URL = (url1+'?'+orgNo+'&'+orderNo2+'&'+platNo1)
print(ra)
#print(URL)

driver = webdriver.Chrome('D:\chromedriver.exe')
driver.get(URL)
driver.implicitly_wait(5)
driver.refresh()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div/div[2]/div/input').send_keys(card)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[6]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div/input').send_keys(name)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div/input').send_keys(id_card)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[2]/div/input').send_keys(phon)
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[6]/div[2]/div/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div/input').send_keys(code)
sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div/div/div/i').click()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div[2]/div/input').send_keys(cvn2)
sleep(15)
#提交
#driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/button/span').click()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[5]/button[1]').click()
#driver.quit()
sleep(100)
# js = 'window.open("http://192.168.31.161:28380/test_agent/");' #新窗口
# driver.execute_script(js)
# driver.refresh()
# #driver.find_element_by_xpath('//*[@id="menu"]/div[3]/a').click()
# sleep(10)
driver.quit()
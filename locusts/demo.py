#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:04

import os,time
from locust import HttpUser, TaskSet, task

# 定义用户行为类
class UserBehavior(TaskSet):
    mer = time.strftime('%Y%m%d%H%M%S')
    @task
    def get_login(self):
        self.client.get('/test')
        print('test')
    @task
    def get_post(self):
        self.client.post('/',
                         {
                             "head": {
                                 "mercode": "872290479990169",
                                 "termcde": "08494337",
                                 "termidm": "BM847BHVLZ",
                                 "imei": "BM847BHVLZ",
                                 "sendTime": "20201113112931",
                                 "msgType": "0200",
                                 "version": "01"
                             },
                             "sign": "78FA885CA6A3C47121F06EF8B827A704D68665628AFCAAF40A12D1C794F28A07",
                             "body": {
                                 "client_ip": "127.0.0.1",
                                 "currency": "CNY",
                                 "mer_order_no": self.mer,
                                 "mercode": "872290479990169",
                                 "notify_url": "http://116.228.47.74:50087",
                                 "openid": self.mer,
                                 "order_name": "valentest你好",
                                 "order_time": "20201113112931",
                                 "pay_amount": "1",
                                 "prv_data": "1234567890123456789012345678901234567890",
                                 "sep_flg": "Y",
                                 "termcde": "08494337",
                                 "trancde": "P05",
                                 "trans_type": "AL_JSAPI",
                                 "valid_num": "5",
                                 "valid_unit": "00",
                                 "version": "01"
                             }
                         }
                         )

class WebSiteUser(HttpUser):
    tasks = [UserBehavior]
    max_wait = 2000
    min_wait = 1000

if __name__ == '__main__':
    # os.system('locust -f demo.py --host=http://192.168.31.174:9888')
    os.system('locust -f demo.py --host=http://192.168.20.201:8866')

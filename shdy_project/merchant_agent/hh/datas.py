#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 13:26
from config.configs import Config
from public.mocks import Mock


class Datas():
    '''
    数据封装
    '''
    ip = Config().read_conf('IP','hh代理商平台')
    # def __init__(self):


    def urls(self):
        urls = self.ip + 'fractionalTransfer/qry'
        return urls

    def fenrun(self):
        data = {
            'orgNo': '101',  # 机构号
            'logNo': Mock().get_time()  # 流水号
        }
        return data

if __name__ == '__main__':
    s = Datas().urls()
    print(s)
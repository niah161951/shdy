#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 12:49
from shdy_project.merchant_agent.手机pos.手持pos交易同步 import *
from configs.conf import *

if __name__ == '__main__':
    mercid = {
        Config().read_conf('MERCID', 'AH池商户'):Config().read_conf('terminal','AH'),
        Config().read_conf('MERCID', 'XM池商户'): Config().read_conf('terminal', 'XM'),
        Config().read_conf('MERCID', 'SH池商户'): Config().read_conf('terminal', 'SH'),
    }
    for i,t in mercid.items():
            '''手机pos交易同步接口'''
            pos_pay(i,t)

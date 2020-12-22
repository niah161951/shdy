#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 20:05
from multiprocessing import Process
from shdy_project.merchant_agent.hh.分润转账状态查询接口 import fenrunzhuanzhang

if __name__ == '__main__':
    p = Process(target=fenrunzhuanzhang)
    p.start()
    p.join()
    print('线程结束')
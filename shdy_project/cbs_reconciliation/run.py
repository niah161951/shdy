#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 18:41
import os
from multiprocessing import Process
from public.logs import Log
from shdy_project.cbs_reconciliation.对账批次.创建对账任务 import chuangjian

def proces(test):
    try:
        p = Process(target=test())
        p.start()
        p.join()
        Log().info(f'启动成功线程号：{os.getpid()}')
    except Exception as e:
            Log().error(f'启动失败:{e}')

if __name__ == '__main__':
    proces(chuangjian)
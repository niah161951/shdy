#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:05

import psutil,time,logging
def monitor(seconds):
    print('CPU使用率                                         内存使用率  C盘使用率  进程数')
    cpu = psutil.cpu_freq()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('c:\\')
    proc = psutil.pids()
    logging.info("str(cpu)+'%    '+str(memory.percent)+'%      '+str(disk.percent) + '%     '+str(len(proc))")
    print(str(cpu)+'%    '+str(memory.percent)+'%      '+str(disk.percent) + '%     '+str(len(proc)))
    time.sleep(seconds)
if __name__ == '__main__':

            monitor(3)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/7/9 13:25
import psutil,logging,time

#日志使用需指定级别
logging.basicConfig(level=logging.NOTSET)

def jisuan():
    '''
    性能指标计算， 数据来源nmon
    :return:
    '''
    while True:
        Memtotal = float(input('请输入服务器总内存:'))
        Memfree = float(input('请输入服务器未使用内存:'))
        cached = float(input('请输入服务器磁盘中读取的内容缓存:'))
        buffers = float(input('请输入服务器磁盘中写入的内容缓存:'))
        Memory_usage = (Memtotal - Memfree - cached - buffers)/ Memtotal * 100
        print('内存使用率为%s%%'%Memory_usage)
        total_read = float(input('请输入总读网络流量:'))
        total_write = float(input('请输入总写网络流量:'))
        M = (total_read/1024 - total_write/1024)*8
        print('网络每秒使用带宽:%sM'%M)
        yn = input('是否退出y/n:')
        if yn == "n" or yn == 'N':
            break

def monitor(seconds):
    logging.info('CPU使用率                                         内存使用率  C盘使用率  进程数')
    cpu = psutil.cpu_freq()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('c:\\')
    proc = psutil.pids()
    logging.info(f"{str(cpu)}    {str(memory.percent)}%     {str(disk.percent)}%     {str(len(proc))}")
    time.sleep(seconds)

if __name__ == '__main__':
    # jisuan()
    monitor(3)

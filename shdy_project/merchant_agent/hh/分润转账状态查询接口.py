# -*- coding: utf-8 -*-
# 作者  : 一蓑烟雨任平生
# 时间  : 2020/1/6 11:13
from SHDY.public.requeststest import apitest
from SHDY.merchant_agent.hh.datas import Datas

def fenrunzhuanzhang():
    data = Datas().fenrun()
    url = Datas().urls()
    res = apitest().run_main('post',url,data)
    return res

if __name__ == '__main__':
    fenrunzhuanzhang()


# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/12 17:41
from config.configs import Config
from common.api import Apitest
from public.logs import Log


def chuangjian(i):
    ip = Config().read_conf('IP','cbs对账系统')
    url = ip + 'checkBatch/checkTaskBatch'
    data = {
              "checkChannelConfRef": i,
              "checkDate": "20200727",
              "checkResource": "1",
              "interfaceType": 1
            }
    req = Apitest().run_main('post',url,data)
    try:
        if req['code']=='0000' and req['message'] == 'success':
            print('请求成功')
        else:
            print(f"请求失败，原因{req['message']}")
    except Exception as e:
        Log().error(f'异常原因{e}')

    finally:
        return req

if __name__ == '__main__':
    #15，19 测20200727  21 测 20201126
    # 15,19,21
    ids = [15,19]
    for i in ids:
        chuangjian(i)


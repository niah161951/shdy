# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/12 17:58
from config.configs import Config


def tongzhi():
    pay = [20201126,20200727]
    for  i in pay:
        ip = Config().read_conf('IP','cbs对账系统')
        url = ip + 'checkBatch/checkResultNotify'
        data = {
                "checkBatchId":802139543259054080,
                "checkDate":i,
                "checkResource":"1",
                "interfaceType":1,
                "restartFlag":0
                }
        req = Apitest().run_main('post',url,data)
        try:
            if req['code'] == '0000' and req['message'] == 'success':
                print('请求成功')
            else:
                Log().error(f"请求失败,原因：{req['message']}")
        except Exception as e:
            Log.error(f'请求异常{e}')
        finally:
            Log().info(f'响应值{req}')
if __name__ == '__main__':

    tongzhi()
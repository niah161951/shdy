#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 9:43
from config.configs import Config


def chongshi():
    checkBatchId = ['802139543259054080', '802137546099261440', '801709320679981872']
    for i in checkBatchId:
        ip = Config().read_conf('IP','cbs对账系统')
        url = ip + 'checkBatch/startCheck'
        data = {
                "restartFlag":1,
                "checkBatchId":i,
                "checkResource":"1"
                }

        req = Apitest().run_main('post', url, data)
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
            chongshi()

# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/3 13:58
import time
from common.api import Apitest
from configs.conf import Config
from public.logs import Log
from public.mocks import Mock

def pos_pay(i,t):
        orderTime = Mock().get_time()
        times = time.strftime('%Y%M%D')
        # print(times)
        ip = Config().read_conf('IP','手机pos')
        url = ip + 'tel/pos'
        data = {
                    "crdNo": "620522003352912760",
                    "mercId": Config().read_conf('MERCID','快速商户'+times),
                    "orgId": '113',
                    "transAmt": 10,#元
                    "transFee": '0.4',#固定手续手续费金额单位元
                    "orderId": orderTime,
                    "seqNo": orderTime,
                    "orderTime": orderTime,
                    "isFirst": 0,  # 是否首刷交易 0：非首刷 1：首刷
                    "transFlag": 'D0',
                    "tranCode": "MP001",
                    "uniMercId": i,
                    "trmNo": t,
                    "acqNm": "哈哈哈10",
                    "payType": "0",
                    "posEmCode": "072",
                    "acqNo": "132323",
                    "uniBatNo": "000139",
                    "referNo": "000100",
                    "uniSeqNo": "000005",
                    "setDate": "20191112",
                    "chaSeqNo": "12312421",
                    "cadFlg": "1",
                    "transType": "1",
                    "baseStation": "460|1|1|1",
                    "sign": "NH3eB2v2F0heXdJscVnAA6PkT9piYugpR5ZF78nNTESugBX+wYr+AtbpP6bNYP70GEJKeosbam3EiqcJuLlPujfowftOBwVBL4lFoErtmjoFRBJaV2Q96sngFyy1J9l7kGWuFQilFN+hnmC4hIEhrY34Qr9F00lVebiW1ZaTnvg="
                }
        try:
            req = Apitest().run_main('post',url,data,ver='v')
            if req['code']=='000000' and req['msg']=='success':
                seqNo = req['seqNo']
                print('请求成功')
                Log().info(f'{seqNo}')
            else:
                Log().info(f"请求失败,原因：{req['msg']}")

        except Exception as e:
            Log().error(f'异常原因{e}')

        finally:
            return req

# if __name__ == '__main__':
#     mercid = {
#         Config().read_conf('MERCID', 'AH池商户'):Config().read_conf('terminal','AH'),
#         Config().read_conf('MERCID', 'XM池商户'): Config().read_conf('terminal', 'XM'),
#         Config().read_conf('MERCID', 'SH池商户'): Config().read_conf('terminal', 'SH'),
#     }
#     for i,t in mercid.items():
#             pos_pay(i,t)


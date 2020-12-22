#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 11:28
from config.configs import Config
from public.mocks import Mock

def posjinjina():
    IP = Config().read_conf('IP', 'swagger')
    url = IP + "FastMerchantIncoming/pos/inComing"
    data = {
            "synType": "0",  # 0-新增 1-修改
            "bnkAcnm": "测试",  # 银行开户名称
            "busAddr": "上海张江",  # 营业地址
            "crpExpDtD": "2099-01-01",  # 证件过期日期
            "crpIdNo": Mock().get_card(),
            "crpIdTyp": "0",
            "crpNm": "测试",
            "devId": "868145017549928",
            "ip": "180.164.182.174",
            "mccCd": "7999",
            "mercAbbr": "商户简称",
            "mercCity": "郑州市",
            "mercCnm": "商户名称",
            "mercCounty": "二七区",
            "mercId": Mock().get_random(),
            "mercMbl": "13789008900",
            "mercProv": "河南省",
            "orgNumber": "113",
            "seqNo": Mock().get_time(),
            "sign": "string",
            "stlOac": "6228480812341234",
            "stlSign": "1",  # 结算账号公私标志
            "stlWcLbnkNo": "102100099988",
            "usrOprEmail": "test@qq.com"
        }
    try:
            mercId = Apitest().run_main('post', url, data)
            if mercId['msg']=='success' and mercId['code']=='000000':
                return mercId['mercId']
            else:
                Log().error('进件失败')
    except Exception as e:
            Log().error(f'异常原因{e}')

if __name__ == '__main__':
    Config().set_conf('MERCID','快速商户',posjinjina())


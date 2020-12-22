# -*- coding: utf-8 -*-
# @Author  : 一蓑烟雨任平生
# @Time    : 2020/12/20 13:04
from common.ui import *
from configs.conf import *
url = Config().read_conf('IP','uiadm')
dr = WebuiKeys('chrome',url)

cooks =  [
    {
    'domain': 'ser.uat.sh.dy',
    'secure': False,
    'httpOnly': False,
    'name':'JSESSIONID',
    'value':'F51A094D19C8C1C810C7D86D3214F5C5',
    'path':'/mrbui'
    },
    {
    'domain': 'ser.uat.sh.dy',
    'secure': False,
    'httpOnly': False,
    'name':'DYMBUTOKEN',
    'value':'mbu_session_F3DA82EAB219B40058224C994E6BD428',
    'path':'/mrbui'
    }
]
dr.get_add_cookie(cooks)
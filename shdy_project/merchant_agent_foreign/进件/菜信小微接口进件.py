#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 14:43
from SHDY.public.configtest import Config
from SHDY.public import requeststest
from SHDY.public.data_test import Mock

ip = Config().read_conf('IP','swagger')
url = ip + 'microMerchant/in'


date = {
          "agentNumber": "162",
          "bnkAcnm": "菜信网",
          "busAddr": "上海市",
          "crpExpDtD": "2025-09-30",
          "crpIdNo": "110000199001011112",
          "mccCd": "7999",
          "mercAbbr": "菜信网",
          "mercCity": "2900",
          "mercCnm": "菜信网",
          "mercCounty": "2904",
          "mercMbl": "13222222229",
          "mercProv": "2900",
          "orgNumber": "162",
          "outMercId": "90998773100928",
          "seqNo": Mock().get_time(),
          "settType": "3",
          "sign": "ZL1v07SqzLW7JYsBR5INqI3p02WZCLdTUSFHP+4Idfc84Lhc7FpbjTaCDGnlqduUU9/a8H5CGba3hmqYwNaPLfNrz5eSaaEdyy7Ps6/akFHIi5V8/tqWrBoZMPANtLE4mTGuACwWppD14Fe5zhn7JeYbtV9RTAlxdI696PNlic8=', crpExpDtD='2025-09-30', stlWcLbnkNo='102110010037', stlOac='BkwkkZNlGwN2p+0197MxBZ1A2KA5U9/iNm/k79J5eN2jg0w4I1dtDI2MdkYw/kIQXJXLtQPdhm3+dChFI5QVDvvothDU9iVoU68bN+nLunFVrKzu8V2nOhUj2KwwXJ8O0kjYu6Qh7dfGBLqmUi0aXe8J2iQ4Tc8dIlglWEYNFRY=', bnkAcnm='zTCRZfCdY+BxgFyAFOCscTq+6XoQCvrLdPq4o1tYEKZft678bynlPn1y0n74f0DOzorzHQdWmJPSvipOeTsSdPaKK2e0ZZ6grOjbKo4m8Gg/sTMdQeRAQFnnrkjaiTvK+LvrgTISLqtEpgmoeGvCZNqPDNm9K4ETSud0P82oHNg=', outMercId='90998773100928', settType='3', subAccFlg='null', sign='UigdL3aDOUFP4hdSp7JOAfHqX/HDwava+vdPTHhyodaOt74ypj/qKEX/olkzf3JGaqlhEFjpwAwhf7VjXmvNjMsFVtnC1u1hFo/HQP43iJ13Oo8Mmz1UH2n9kMzgjx32Jl+0rKOzRQfAuzA22vc186zejQSnJseP012BijRRxQ4=",
          "stlOac": "6226095950521497",
          "stlWcLbnkNo": "102110010037",
          "subAccFlg": ""
}

requeststest.apitest().run_main('POST',url,date)
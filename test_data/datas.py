#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:09
from configs.conf import *


class Data:
    '''
    数据封装
    '''
    url = Config().read_conf('IP', '绑卡')

    def __init__(self):

        self.data = {
            "requestFrontUrl": "https://gateway.test.95516.com/gateway/api/frontTransReq.do",
            "requestDatas": {
                "bizType": "000301",
                "txnSubType": "00",
                "backUrl": "http://117.186.119.42:50080/bkg/f/ahacpb.acpb",
                "signature": "uYuWzkrdJMZygi91LdKge/Htfy4KGks/pM3XFDvQ0mnUAMlNUCijK7bKpXwxjOJmSJZ9nvimgz86kAcATUJqQ1TXULJ41w9v21flh3DsvH0UpfD99UxV9zFHjLHea6/F3FfQWkfZe+rMu23QV0WhuYj67B5eLugriTZNbsykA9LfysMUwHo2dbL4KZW10SlZHxvN2dSzlAEdmvxBRly5PaFk+sJVn7N+c9cV23ZCKSRD+W4YF1be0B3BmcNC/gS69O7VG2heO/RU3E9auclibmLlKIxN36F5LUPUZP6nqx80vvkXO0PoK6IKvqjvcJrtFdU0eutqs5KDClHwFVKcnw==",
                "orderId": "202008250057186991",
                "accNo": "o/q6J3EMfX78o42FXU3kidd0DFS+Y7Onoi/VD95wTKulVz5eIc1/69+kLmYUpVckOD6NRqNr7SZug7UQ1exIpjcsNgpLU/XatUw/6LRAcMOatqL2fX29KGKMW6bOScric2p04vAPTQtah6FI+iMph+x2TO+/92UznF0zTN0kSDN3PMEjACpK6tplt5v/Vrd9xVXY5Fv+V6ZF6sLf5aKThK23tf09Abl6RLXJbVdHQfyeK/TKdU/ZyoHiUqyOSmUu6v1XpDjz/D8Uwe7dEyw1Lm1Wlp4VnfkoAeUU5zC2OnXViNuMcynzRAnBeLT6QH9yogA96dtdD6nk10aLc5uHrw==",
                "customerInfo": "e2NlcnRpZlRwPTAxJmNlcnRpZklkPTM0MTEyNjE5NzcwOTIxODM2NiZjdXN0b21lck5tPeWFqOa4oOmBkyZlbmNyeXB0ZWRJbmZvPVhxR0tTZ21uVzR1aGoxMEx6aHl4L1M1TFFFRXNNdlJSMG9PTE9oaE80Yys5WG1GbXpOTFk3bHAvUEM5Sk1aSGYyQitoR3MveElydHlQLytFdXdZUHVHWDF5ZlJpTFZ1NUFnOU5pVFpVTVk1WmtRMUdyQUtCOUZLYS9pYnBheUI0cnJpRDY4SHdGelZLWnpyVWs5OEdFWGFzd3p4c1cxcGd4WHc3dkNUWFgwRGRGR0cyZktLUENIYW5kVksycUJER1dxSXUxd0JLTURsT1l2aEEwRlR5NUVlV21pWkdLMkMyOGRCNlp2d1BlN2phRHpkTThiRlB0TVdZZWs1c2Q5SHRNUktBdmF2a1JROE1LNU5XajVkU0lYb3pMQnhaZkJrY2dtUitQN2RpeEo5MXdDQktuTEV1QWFOR0M4THhyenVpZHY2b01NbTM2a1NZM09HcEdqREVJZz09fQ==",
                "txnType": "79",
                "frontUrl": "http://117.186.119.42:50080/bkg/f/ahacp.acpf",
                "channelType": "07",
                "certId": "69629715588",
                "encoding": "UTF-8",
                "version": "5.1.0",
                "encryptCertId": "69026275926",
                "accessType": "0",
                "txnTime": "20201210143715",
                "merId": "872331873925001",
                "signMethod": "01"
            }

        }

    def bangka(self):
        return self.data
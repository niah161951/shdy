# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/11 16:01

import requests
from SHDY.public.conf_test import Config

dyMchNo = Config().get_param("mercid")
dyMchNo1 = Config().get_param("id")
seqNo = Config().get_param("seqno")
#token = Config().get_param("token")
url = 'http://localhost:8080/DemoJava/cardSign/cardRelieve'
data =  {
            'orgNumber':'121',           #机构号
            'dyMchNo':dyMchNo1,           #电银商户号
            'seqNo':seqNo,           #流水号  绑卡返的
            'token':'c53f8005f53444ae97070620634ff6ed',           #绑卡token  绑卡返的
            'sign':''              #签名

}
reg = requests.post(url,json=data).json()
print(reg)


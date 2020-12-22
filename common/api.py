#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/7/6 18:25
import requests,json
from public.logs import Log

class Apitest:
    '''
    requests 二次封装
    '''

    def post_main(self, url, data, ver=None,file=None, header=None,cookies=None,timeout=None,auth=None):
        '''
        post 请求封装
        :param url:
        :param data:
        :param ver:
        :param file:
        :param header:
        :param cookies:
        :param timeout: 响应时间控制
        :param auth 用户名鉴权
        :return:
        '''
        try:
            if header is not None:
                res = requests.post(url, json=data,files=file, headers=header,verify=False)
            elif ver is not None :
                res = requests.post(url, json=data,verify=False)
            else:
                res = requests.post(url, json=data)
            Log().info(f'返回数据：{res.text}\n接口耗时：{res.elapsed.total_seconds()}s')
            return res

        except Exception as error:
            Log.error(f'异常原因：{error}')
            return 444

        finally:
            Log().info(f'请求值:\n{url}\n{data}\n{ver}\n{header}')

    def get_main(self,url, data=None, ver=None, header=None):
        '''
        get请求封装
        :param url:
        :param data:
        :param header:
        :return:
        '''
        try:
            if header is not None:
                res = requests.get(url, params=data, headers=header,verify=False)
            elif ver is not None:
                res = requests.get(url, params=data,verify=False)
            else:
                res = requests.get(url, params=data)
            Log().info(f'返回数据：{res.text}\n接口耗时：{res.elapsed.total_seconds()}s')
            return res

        except Exception as error:
            Log.error(f'异常原因：{error}')
            return 400
        finally:
            Log().info(f'请求值:\n{url}\n{data}\n{ver}\n{header}')

    def api_updata(self,method,url,file,data=None,ver=None):
        try:
            res = requests.request(method,url,files=file,data=data).json()
            req = json.dumps(res,indent=4,ensure_ascii=False,sort_keys=True)
            Log().info(f'上传接口：{req}')
            return res
        except Exception as e:
            Log().error(f'异常原因：{e}')

    def run_main(self, method, url,data=None,text=None, ver=None, header=None):
        '''
        请求
        :param method:
        :param url:
        :param data:
        :param header:
        :return:
        '''
        try:
            if method in ['post','POST']:
                if text is not None:
                    res = self.post_main(url, data).text
                    Log().info(f'{method} 方式响应格式化：{res}')
                    return res
                else:
                    if ver is not None:
                        res = self.post_main(url, data,ver, header).json()
                        req = json.dumps(res, indent=4, ensure_ascii=False, sort_keys=True)
                    else:
                        res = self.post_main(url, data).json()
                        req = json.dumps(res, indent=4, ensure_ascii=False, sort_keys=True)
                    Log().info(f'{method} 方式响应格式化：{req}')
                    return res

            elif method in ['get','GET']:
                res = self.get_main(url, data, header).json()
                req = json.dumps(res, indent=4, ensure_ascii=False, sort_keys=True)
                Log().info(f'{method} 方式响应格式化：{req}')
            else:
                Log().info('请输入：GET、POST请求')
            return res

        except Exception as error:
            Log.error(f'返回失败原因：{error}')


if __name__ == '__main__':

    def method_name():
        url = "http://192.168.31.161:18380/transaction_agent/card/createHTML"
        data = {
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
        Apitest().run_main('post', url, data, 's')


    method_name()





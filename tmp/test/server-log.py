# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/10/21 13:23
import paramiko,re

def get_key():
    client = paramiko.SSHClient()
    host_ip='192.168.31.161'
    port=22
    username='shdy'
    password='shdy123'
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while True:
        try:
            client.connect(host_ip, port, username, password, timeout=100)
            print("链接成功")
            # 执行命令，#stdin =>  标准输入，就是你输入的那个命令
            # stdout => 标准输出，你输入命令后执行的结果
            # stderr => 标准错误，名利执行的过程中，如果出错了，就把这个错误打到这里
            stdin,stdout,stderr = client.exec_command('sudo su - ')
            # stdin,stdout,stderr = client.exec_command('cdl')
            #5.获取命令执行的结果
            stdin,stdout,stderr = client.exec_command('tail -1000f /home/wtposp/logs/wtposp.log')
            result=stdout.read().decode('utf-8')
            print("执行成功")
            before = '本地签名,用于调试：'
            after = '='
            lookingfor = before + '(.*)' + after
            print(result,lookingfor)
            import time
            time.sleep(10)

            if '本地签名' in result:
                res = re.findall(lookingfor, result)[0]+'='
                # 关闭链接
                # client.close()
                break
            else:
                print("未找到 key")
                # fenzhang()
        except:
            print("进行 新一轮 链接，请稍后")
    print(res)
    return res

if __name__ == '__main__':
    get_key()
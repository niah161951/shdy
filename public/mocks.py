# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/24 9:32
import time
from faker import Faker

class Mock:
    """
    address 地址
    person 人物类：性别、姓名等
    barcode 条码类
    color 颜色类
    company 公司类：公司名、公司email、公司名前缀等
    credit_card 银行卡类：卡号、有效期、类型等
    currency 货币
    date_time 时间日期类：日期、年、月等
    file 文件类：文件名、文件类型、文件扩展名等
    internet 互联网类
    job 工作
    lorem 乱数假文
    misc 杂项类
    phone_number 手机号码类：手机号、运营商号段
    python python数据
    profile 人物描述信息：姓名、性别、地址、公司等
    ssn 社会安全码(身份证号码)
    user_agent 用户代理
    补充
    https://www.jianshu.com/p/6bd6869631d9
    """
    mc = Faker('zh_CN')

    def get_name(self):
        """
        随机姓名
        :return:
        """
        return self.mc.name()

    def get_username(self):
        """
        随机用户名
        :return:
        """
        return self.mc.user_name()

    def get_phone(self):
        """
        随机手机号
        :return:
        """
        return self.mc.phone_number()

    def get_bankCar(self):
        """
        随机银行卡
        :return:
        """
        return self.mc.credit_card_number()

    def get_barcode(self):
        """
        获取随机条码码
        :return:
        """
        return self.mc.user_name()

    def get_email(self):
        """
        获取随机邮箱号
        :return:
        """
        return self.mc.free_email()

    def get_password(self):
        """
        获取随机密码
        :return:
        """
        return self.mc.password()

    def get_time(self):
          '''
          日期订单号
          :return:
          '''
          date = time.strftime("%Y%m%d%H%M%S")
          return date

    def get_random(self):
        """
        随机数-流水号
        :return:
        """
        random_number = self.mc.random_int(min=000000000000000,max=999999999999999)
        return random_number

    def get_card(self):
        '''
        生成身份证号
        :return:
        '''
        return self.mc.ssn()

    def get_Company(self):
        '''
        公司名字
        :return:
        '''
        return self.mc.company()

    def get_card_number(self):
        '''
        信用卡号
        :return:
        '''
        return self.mc.credit_card_number()

    def get_address(self):
        '''
         地址
        :return:
        '''
        address = self.mc.province() +  self.mc.street_address()
        return address

    def get_user_agent(self):
        '''
        用户代理
        :return:
        '''
        aget = self.mc.user_agent()
        return aget

    def get_domain_name(self):
        '''
        生成域名
        :return:
        '''
        return self.mc.domain_name()
    def get_ipv4(self):
        '''
        随机IP4地址
        :return:
        '''
        return self.mc.ipv4()
    def get_url(self):
        '''
        随机URI地址
        :return:
        '''
        return self.mc.uri()

if __name__ == '__main__':
    m = Mock()
    s = m.get_url()
    print(s)
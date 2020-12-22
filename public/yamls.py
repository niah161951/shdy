# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/8/15 15:08
import os,yaml
from public.logs import Log

class YamlTest:
    def __init__(self):
        self.filepath = os.path.split(os.path.dirname(__file__))[0]
        self.yamlPath = os.path.join(self.filepath,'configs.yaml')
        Log().info(f'获取地址成功：{self.yamlPath}')

    def setadd(self, model, **kwargs):
        '''
        文件模式
        :param model:
        w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        r+	打开一个文件用于读写。文件指针将会放在文件的开头。
        :return:
        '''
        try:
            fb = open(self.yamlPath,f'{model}',encoding='utf-8')
            yaml.dump(kwargs, fb)
            Log().info(f'输入model：{model}\n输入数据dict：\n{kwargs}')
        except Exception as error:
            Log().error(f'失败原因：{error}')

    def get_read(self,model,titel=None,ftb=True):
        '''
        读取文件
        :param model:
        :return:
        '''
        try:
            fb = open(self.yamlPath,f'{model}',encoding='utf-8')
            cont = fb.read()
            if ftb:
                rd = yaml.load(cont,Loader=yaml.FullLoader)
                titels = rd.get(titel)
                typetest = type(titels)
                Log().info(f'输入model：{model}\n获取数据values：{titels}\n'
                           f'获取数据类型：{typetest}')
                return titels

            elif not ftb:
                all_data = yaml.load_all(cont, Loader=yaml.FullLoader)
                for i in all_data:
                    Log().info(f'输入model：{model}\n获取数据values：{i}')
                return i
        except Exception as error:
            Log().error(f'失败原因：{error}')

if __name__=="__main__":
    yal = YamlTest()
    data = {'school': 'zhu',
            'students': 'b'}
    stryal = yal.get_read('r',ftb =False)
    s = stryal
    print(s)


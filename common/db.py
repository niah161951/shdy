import cx_Oracle
import pymysql
from configs.conf import Config
from public.logs import Log

class MysqlDB:

    def __init__(self):
        self.cursor = None
        self.conn = None
        self.db = Config().read_conf('DB','database')
        self.host = Config().read_conf('DB','host')
        self.user = Config().read_conf('DB','user')
        self.password = Config().read_conf('DB','password')
        self.charset = 'utf8'
        self.port = 3306


    def connect(self):
        try:
            con = pymysql.connect(
                database=self.db,
                host=self.host,
                user=self.user,
                password=self.password,
                charset=self.charset,
                port=self.port
            )
        except Exception as e:
            Log.info(f'失败原因：{e}')
            return False
        return con

    def _cursor(self):
        cursor = self.connect().cursor()
        if cursor:
            return cursor
        raise ConnectionError

    def execute(self, sql):
        self.cursor = self._cursor()
        self.cursor.execute(sql)
        Log().info(f'请输入sql：{sql}')

    @staticmethod
    def to_json(result):

        _list = []

        for l in result:
            _list.append(list(l))
        return _list

    def sql_fetch_json(self):

        keys = []
        for column in self.cursor.description:
            keys.append(column[0])
        key_number = len(keys)

        json_data = []
        for row in self.cursor.fetchall():
            item = dict()
            for q in range(key_number):
                item[keys[q]] = row[q]
            json_data.append(item)
        self.cursor.close()
        Log().info(f'执行函数sql_fetch_json返回字典结果：{json_data}')
        return json_data

    def closed(self):
        self.cursor.close()
        Log().info(f'关闭{self.host}数据库连接成功')

class ORACLE(MysqlDB):
    '''
    oracle 二次封装
    '''
    def __init__(self):
        self.host = Config().read_conf('base','host')
        self.user = Config().read_conf('base','user')
        self.pwd = Config().read_conf('base','password')
        self.db = Config().read_conf('base','db')
        # self.host = host
        # self.user = user
        # self.pwd = pwd
        # self.db = 'ORCL'
        self.cursor = None
        self.conn = None

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = cx_Oracle.connect(self.user + '/' + self.pwd + '@' + self.host + '/' + self.db)
        cursor = self.conn.cursor()
        if not cursor:
            raise (NameError, "连接数据库失败")
        else:
            return cursor

    def _cursor(self):
        cursor = self.__GetConnect()
        if cursor:
            return cursor
        raise ConnectionError


if __name__ == '__main__':
    # db = MysqlDB()
    # trun = "select id from t_merchant_info  where dy_mch_no = {};".format('872112378410001')
    # db.execute(trun)
    # res = db.sql_fetch_json()
    # res = res[0]['id']
    # print(res)
    # db.closed()
    db = ORACLE()
    sql = ''
    db.execute(sql)
    req = db.sql_fetch_json()
    req = req[0]['MAL_SUB']

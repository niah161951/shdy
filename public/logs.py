#coding=utf-8
import logging,os,time
from logging.handlers import RotatingFileHandler


class Log(object):

    def __init__(self):
        '''初始化'''

        # 时间戳
        self.time_fb = time.strftime('%Y%m%d')
        # 日志存放目录
        self.log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.logs_path = os.path.join(self.log_path, 'logs')
        if not os.path.exists(self.logs_path):
            os.makedirs(self.logs_path)
        time_fb = time.strftime('%Y%m%d')
        self.log_file = os.path.join(self.logs_path,time.strftime(time_fb + '.log'))

    def _public(self,level,message):
        # 创建一个logger
        logger = logging.getLogger()
        #级别低不打印日志
        logger.setLevel(logging.DEBUG)

        # 创建日志文件存在路径
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.log_file,'a',encoding='utf-8')
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        # self.fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        self.fmt = '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
        self.format_str = logging.Formatter(self.fmt)
        fh.setFormatter(self.format_str)
        ch.setFormatter(self.format_str)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        try:
            # 记录一条日志
            if level == 'info' or level == 'INFO':
                logger.info(message)
            elif level == 'debug' or level == 'DEBUG':
                logger.debug(message)
            elif level == 'warning' or level == 'WARNING':
                logger.warning(message)
            elif level == 'error' or  level == 'ERROR':
                logger.error(message)
        except  Exception as error:
            print(f'未知错误{error}')
        finally:
        # 记录完日志移除句柄Handler
            logger.removeHandler(ch)
            logger.removeHandler(fh)
            # 关闭打开文件
            fh.close()

    def debug(self,message):
        self._public('debug',message)

    def info(self, message):
        self._public('info', message)

    def warning(self, message):
        self._public('warning', message)

    def error(self, message):
        self._public('error', message)

if __name__ == '__main__':
    log = Log()
    log.error('请输入')
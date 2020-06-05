#coding=utf-8

import logging
import time
import commonparameter

class Log:
    def __init__(self):
        self.logname = commonparameter.log_path + '\\' + 'Log' +time.strftime('%Y-%m-%d') + '.log'

    def printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger('mylogger')
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname,'a')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self,message):
        self.printconsole('debug', message)

    def info(self,message):
        self.printconsole('info', message)

    def warning(self,message):
        self.printconsole('warning', message)

    def error(self,message):
        self.printconsole('error', message)

if __name__ == '__main__':
    log = Log()
    log.info('info msg1000013333')
    log.debug('debug msg')
    log.warning('warning msg')
    log.error('error msg')
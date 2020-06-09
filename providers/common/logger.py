#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/13 14:04
# @Author  : Soner
# @version : 1.0.0


import os

try:
    from loguru import logger
except ImportError as I:
    conne = os.popen("pip install loguru").read()
    if conne:
        if "Successfully" in conne:
            from loguru import logger
        else:
            raise ImportError
import time


now = time.strftime("%Y-%m-%d")


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        #  获取项目根目录
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # 判断以当前时间命名的文件夹是否存在，不存在则新建
        self.LOG_ROOT = "{}/logs/{}".format(BASE_DIR, now)
        if not os.path.exists(self.LOG_ROOT):
            os.makedirs(self.LOG_ROOT)
        self.log_bind = logger.bind(task=file_name)

    def getlog(self):
        self.log = logger
        # retention: 设置日志有效时长   enqueue:异步写入
        self.log.add(
            "{}/{}.log".format(self.LOG_ROOT, self.file_name),
            colorize=True,
            format="<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g> | <c>{level: <7}</c> | <e>{file}</e> | <m>{function}()</m> | <yellow>{line: <4}</yellow> | 消息：<lvl>{message}</lvl>",
            enqueue=True,
            retention="2 days",
            encoding="utf-8",
            backtrace=True,
            diagnose=True,
            catch=True,
            filter=lambda record: record["extra"]["task"] == self.file_name,
        )

        return self.log_bind


def error_format(e):
    """
    格式化error错误
    @param e:
    @return:
    """
    line = e.__traceback__.tb_lineno
    file = e.__traceback__.tb_frame.f_globals["__name__"]
    return "发生错误的文件：{}，行数：{}，错误：{}".format(file, line, repr(e))


if __name__ == "__main__":
    # logger.remove()
    # lo1 = logger.bind(task='123')
    log = Logger("123").getlog()
    log.info("sfs2")
    log.error("232")

    log2 = Logger("12").getlog()
    log2.info("test")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3
# @Author  : Soner
# @version : 1.0.0

import unittest
import datetime
from providers.common.set_driver import driver_setup
from providers.common.base_operation import Operation
from providers.common.preprocessing import Preprocessing
from providers.account.account import Account


class BaseClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_time = datetime.datetime.now()
        cls.driver, cls.udid, cls.log = driver_setup()
        cls.preprocessing = Preprocessing(cls.driver, log=cls.log)
        # 跳过首页引导
        cls.preprocessing.skip_guide()
        # 点击同意用户协议
        cls.preprocessing.agree_license()
        # 跳过升级弹窗
        cls.preprocessing.cancel_update()
        # 跳过监控日报
        cls.preprocessing.skip_monitor()

        # 获取基础操作
        cls.operation = Operation(cls.driver, log=cls.log)
        # 获取账号操作
        cls.account = Account(log=cls.log)

    def setUp(self):
        pass

    def tearDown(self):
        self.preprocessing.back_index()


    @classmethod
    def tearDownClass(cls):
        end_time = datetime.datetime.now()
        time_all = (end_time - cls.start_time).total_seconds()
        m, s = time_all//60, time_all%60
        h, m = m // 60, m % 60
        cls.log.info('========== 设备：{} 用例集执行完毕，共用时 {}时 {}分 {}秒 ==========\n\n\n'.format(cls.udid, int(h), int(m), int(s)))
        cls.driver.quit()

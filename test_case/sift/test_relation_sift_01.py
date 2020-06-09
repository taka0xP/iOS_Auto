# -*- coding: utf-8 -*-
# @Time    : 2020-05-26 15:37
# @Author  : XU
# @File    : test_relation_sift_01.py
# @Software: PyCharm
import time
import unittest
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import Logger, error_format
from providers.common.base_client import BaseClick
from providers.sift.operation import SiftOperation
from providers.sift.process import SiftProcess

log = Logger("查关系-筛选01").getlog()


class TestRelationSift01(BaseClick):

    vip_num = None

    def setUp(self):
        self.sift_operate = SiftOperation(self.driver)
        self.elements = self.sift_operate.get_element()
        self.sift_process = SiftProcess(self.driver)

    def test_relation_sift_001(self):
        """查关系：更多筛选，搜索范围"""
        log.info(self.test_relation_sift_001.__doc__)
        try:
            self.vip_num = self.account.get_account(account_type='vip')
            vip_passwd = self.account.get_pwd()
            self.preprocessing.login(self.vip_num, vip_passwd)
            self.sift_process.random_key("特斯拉", "商标")
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["shangbiao"]).text
            self.assertIn("特斯拉", text)
        except Exception as e:
            log.error(format(e))

    def test_relation_sift_002(self):
        """查关系：更多筛选，搜索范围"""
        log.info(self.test_relation_sift_002.__doc__)
        try:
            self.sift_process.random_key("特斯拉", "商标")
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["shangbiao"]).text
            self.assertIn("特斯拉", text)
        except Exception as e:
            log.error(format(e))
        finally:
            self.account.release_account(self.vip_num, account_type='vip')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6
# @Author  : Soner
# @version : 1.0.0


import unittest
from random import randint
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import error_format
from providers.common.base_operation import getimage
from providers.common.base_client import BaseClick
from providers.all_services.operating import ServerOperating
from providers.common.read_data import ReadExcel


class TestAllServerCheckSearchPhone(BaseClick):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 获取excel
        cls.excel = ReadExcel().read_excel("all_server")
        cls.server_oper = ServerOperating(driver=cls.driver,
                                          excel=cls.excel,
                                          log=cls.log)

    def setUp(self):
        # 点击 「全部」
        self.server_oper.click_all()
        # 点击「找电话」
        self.server_oper.click_server("身边老板")
        # 首次进入过引导
        self.server_oper.aroundf_boss()

    @getimage
    def test_sy_jgq_aroundf_boss_001(self):
        "首页金刚区-热门功能-身边老板，通讯录中没有号码，检验 占位标识"
        self.log.info(self.test_sy_jgq_aroundf_boss_001.__doc__)
        try:
            diff_remind = "没有发现通讯录中的老板"
            find_remind = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['aroundf_boss_remind']).text
            self.assertEqual(diff_remind, find_remind, "预期值：{}，实际值：{}".format(diff_remind, find_remind))

            diff_recommend = "为你推荐"
            find_recommend = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                        self.excel['aroundf_boss_recommend']).text
            self.assertEqual(diff_recommend, find_recommend, "预期值：{}，实际值：{}".format(diff_recommend, find_recommend))

            diff_monitor_button = "一键监控"
            find_monitor_button = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                             self.excel["aroundf_boss_monitor_button"]).text
            self.assertEqual(diff_monitor_button, find_monitor_button,
                             "预期值：{}，实际值：{}".format(diff_monitor_button, find_monitor_button))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_aroundf_boss_002(self):
        "首页金刚区-热门功能-身边老板，通讯录中没有号码，点击一键监控/监控未登录拉起登陆"
        self.log.info(self.test_sy_jgq_aroundf_boss_002.__doc__)
        try:
            msg = "短信验证码登录"
            # 获取「一键监控」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel["aroundf_boss_monitor_button"]).click()
            login_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title']).text
            self.assertEqual(msg, login_title, "预期值：{}，实际值：{}".format(msg, login_title))

            # 点击「返回」
            self.preprocessing.backtrack()

            # 获取「监控」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['aroundf_boss_monitor'].format(4)).click()
            login_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title']).text
            self.assertEqual(msg, login_title, "预期值：{}，实际值：{}".format(msg, login_title))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_aroundf_boss_003(self):
        "首页金刚区-热门功能-身边老板，通讯录中没有号码，校验「监控」功能"
        self.log.info(self.test_sy_jgq_aroundf_boss_003.__doc__)
        try:
            user = self.account.get_account()
            # 获取「推荐列表第一个名字」
            boss_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                   self.excel['aroundf_boss_name'].format(4)).text
            # 点击「监控」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['aroundf_boss_monitor'].format(4)).click()
            # 登录
            login_status = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title'])
            if login_status:
                self.preprocessing.login(phone_num=user, password=self.account.get_pwd())
                # 点击「监控」
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                           self.excel['aroundf_boss_monitor'].format(4)).click()
            # 跳过 监控日报 邮箱设置
            self.preprocessing.skip_monitor_daily_email()
            # 进入到 监控列表
            self.preprocessing.enter_monitor_list()
            # 获取监控列表
            groups = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['monitor_list']))
            self.assertTrue(groups > 1, "监控列表为空，未监控上")
            flag = False
            for i in range(1, groups + 1):
                monitor_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                          self.excel['monitor_list_info'].format(i)).text
                if monitor_name == boss_name:
                    flag = True
                    break
            self.assertTrue(flag, "监控列表未找到刚关注的人：{}".format(boss_name))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e
        finally:
            self.account.release_account(user)


if __name__ == '__main__':
    unittest.main()

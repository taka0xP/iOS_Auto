#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7
# @Author  : Soner
# @version : 1.0.0


import unittest
import time
from random import randint
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import error_format
from providers.common.base_operation import getimage
from providers.common.base_client import BaseClick
from providers.all_services.operating import ServerOperating
from providers.common.read_data import ReadExcel


class TestAllServerCheckTycMap(BaseClick):
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
        # 点击「天眼地图」
        self.server_oper.click_server("天眼地图")

    @getimage
    def test_sy_jgq_tyc_map_001(self):
        "首页金刚区-热门功能-天眼地图，校验未登录点击页面条件，跳转登录页"
        self.log.info(self.test_sy_jgq_tyc_map_001.__doc__)
        try:
            msg = "短信验证码登录"
            # 「有手机号码」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有手机号码").click()
            login_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title']).text
            self.assertEqual(msg, login_title, "预期值：{}，实际值：{}".format(msg, login_title))
            # 点击「返回」
            self.preprocessing.backtrack()

            # 「有联系方式」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有联系方式").click()
            login_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title']).text
            self.assertEqual(msg, login_title, "预期值：{}，实际值：{}".format(msg, login_title))
            # 点击「返回」
            self.preprocessing.backtrack()

            # 「有联系邮箱」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有联系邮箱").click()
            login_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_title']).text
            self.assertEqual(msg, login_title, "预期值：{}，实际值：{}".format(msg, login_title))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_tyc_map_002(self):
        "首页金刚区-热门功能-天眼地图，校验地图内页按钮"
        self.log.info(self.test_sy_jgq_tyc_map_002.__doc__)
        try:
            area_button = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "范围")
            self.assertTrue(area_button, "「范围」按钮不存在")

            location_button = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "location nor")
            self.assertTrue(location_button, "「location」按钮不存在")

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_tyc_map_003(self):
        "首页金刚区-热门功能-天眼地图，校验搜索候选列表"
        self.log.info(self.test_sy_jgq_tyc_map_003.__doc__)
        try:
            # 点击 「搜索框」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "输入地点，即可查询周围的公司").click()
            # 输入「搜索词」
            self.operation.send(MobileBy.ACCESSIBILITY_ID, "输入地点，即可查询周围的公司", "百度")
            groups = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map_search_list']))
            for i in range(1, groups + 1):
                search_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                         self.excel['ty_map_search_list_name'].format(i)).text
                self.log.info(search_name)
                self.assertIn("百度", search_name, "搜索列表值：{}".format(search_name))
        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_tyc_map_003(self):
        "首页金刚区-热门功能-天眼地图，校验搜索-一键清除按钮"
        self.log.info(self.test_sy_jgq_tyc_map_003.__doc__)
        try:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "输入地点，即可查询周围的公司").click()
            self.operation.send(MobileBy.ACCESSIBILITY_ID, "输入地点，即可查询周围的公司", "百度")
            groups = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map_search_list']))
            self.log.info("搜索结果数：{}".format(groups))
            # 一键清除
            self.preprocessing.clear_text()
            find_title = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "您可以试试")
            self.assertTrue(find_title, "未找到「您可以试试」")
        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_tyc_map_004(self):
        "首页金刚区-热门功能-天眼地图，校验全部行业随机选择"
        self.log.info(self.test_sy_jgq_tyc_map_004.__doc__)
        try:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "全部行业").click()
            random_name = self.preprocessing.random_options(find_type=MobileBy.IOS_CLASS_CHAIN,
                                                            find_element=self.excel['ty_map_area_one'])
            self.preprocessing.random_options(find_type=MobileBy.IOS_CLASS_CHAIN,
                                              find_element=self.excel['ty_map_area_two'], x=0.46)

            if random_name != "国际组织":
                search_count = self.operation.get_count(find_type=MobileBy.IOS_CLASS_CHAIN,
                                                        find_element=self.excel['ty_map_search_label'])
                self.assertIsNot(search_count, 0, "未匹配到搜索结果数")
            else:
                search_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                         self.excel['ty_map_search_label']).text
                diff_text = "当前范围内没有发现公司，换个位置试试"
                self.assertEqual(diff_text, search_text, "预期文案：{}，实际文案：{}".format(diff_text, search_text))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_tyc_map_005(self):
        "首页金刚区-热门功能-天眼地图，校验非VIP账户，点击VIP条件，调起VIP购买弹窗"
        self.log.info(self.test_sy_jgq_tyc_map_005.__doc__)
        # 获取 非VIP 账号
        user = self.account.get_account()
        try:
            # 判断 登陆状态
            login_status = self.preprocessing.is_login()
            if not login_status:
                self.preprocessing.login(phone_num=user, password=self.account.get_pwd())
                # 点击 「全部」
            self.server_oper.click_all()
            # 点击「天眼地图」
            self.server_oper.click_server("天眼地图")
            msg = "VIP会员可使用高级筛选条件"
            # 「有手机号码」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有手机号码").click()
            vip_title = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, msg)
            self.assertTrue(vip_title, "预期值：{}，实际值：{}".format(msg, vip_title))
            # 点击「关闭」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "ic pop off").click()

            # 「有联系方式」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有联系方式").click()
            vip_title = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, msg)
            self.assertTrue(vip_title, "预期值：{}，实际值：{}".format(msg, vip_title))
            # 点击「关闭」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "ic pop off").click()

            # 「有联系邮箱」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "有联系邮箱").click()
            vip_title = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, msg)
            self.assertTrue(vip_title, "预期值：{}，实际值：{}".format(msg, vip_title))
            # 点击「关闭」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "ic pop off").click()
        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e
        finally:
            self.account.release_account(account=user)

    @getimage
    def test_sy_jgq_tyc_map_006(self):
        "首页金刚区-热门功能-天眼地图，校验非VIP账户，更多筛选，调起VIP购买弹窗"
        self.log.info(self.test_sy_jgq_tyc_map_006.__doc__)
        # 获取 非VIP 账号
        user = self.account.get_account()
        try:
            msg = "VIP会员可使用高级筛选条件"
            # 判断 登陆状态
            login_status = self.preprocessing.is_login()
            if not login_status:
                self.preprocessing.login(phone_num=user, password=self.account.get_pwd())
            # 点击 「全部」
            self.server_oper.click_all()
            # 点击「天眼地图」
            self.server_oper.click_server("天眼地图")
            # 点击「更多筛选」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "更多筛选").click()

            # 「手机号码」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=3)
            # 「联系方式」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=4)
            # 上滑一页
            self.operation.mobile_swipe('up')
            # 「联系邮箱」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=10)
            # 「商标信息」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=11)
            # 「专利信息」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=12)
            # 「软件著作权」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=13)
            # 「作品著作权」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=14)
            # 「融资信息」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=15)
            # 「上市状态」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=16)
            # 上滑一页
            self.operation.mobile_swipe('up')
            # 「500强」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=17)
            # 「失信信息」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=18)
            # 「网址信息」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=19)
            # 「动产抵押」
            self.server_oper.check_vip_popup(find_type=MobileBy.IOS_CLASS_CHAIN, find_element=self.excel['ty_map_more'],
                                             item_num=20)
            # 「底部VIP」
            bottom = self.operation.new_element(MobileBy.IOS_PREDICATE,
                                       "type == 'XCUIElementTypeStaticText' AND name == '购买VIP，使用全部筛选条件'")
            self.operation.mobile_tap(element=bottom)
            self.server_oper.vip_popup(msg=msg)

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e
        finally:
            self.operation.mobile_tap(x=10, y=20)
            self.account.release_account(account=user)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29
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
        self.server_oper.click_server("找电话")

    @getimage
    def test_sy_jgq_search_phone_001(self):
        "首页金刚区-热门功能-找电话，校验热门搜索分栏是否存在，并从热搜进入"
        self.log.info(self.test_sy_jgq_search_phone_001.__doc__)
        try:
            # 校验标签
            hot_search = "热门搜索"
            hot_title = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN, self.excel['hot_search']).text
            self.assertEqual(hot_search, hot_title,
                             "预期值：{}，实际值：{}".format(hot_search, hot_title))

            # 判断 热搜 个数
            hot_set = self.operation.new_elements(
                MobileBy.IOS_CLASS_CHAIN, self.excel['hot_search_group'])
            hot_set_num = len(hot_set)
            self.assertIs(3, hot_set_num,
                          "预期值：{}，实际值：{}".format(3, hot_set_num))

            # 从任意热搜进入
            round_num = randint(0, hot_set_num - 1)
            select_name = hot_set[round_num].text
            # 从选择的热搜进入搜索结果页
            hot_set[round_num].click()
            # 获取搜索词
            result_name = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN, self.excel['search_field']).text
            self.assertEqual(select_name, result_name,
                             "预期值：{}，实际值：{}".format(select_name, result_name))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_002(self):
        "首页金刚区-热门功能-找电话，校验 非常用字符、空值、屏蔽词，搜索无结果"
        self.log.info(self.test_sy_jgq_search_phone_002.__doc__)
        try:
            search_word = "!@#$"
            self.server_oper.check_search_null(MobileBy.IOS_CLASS_CHAIN,
                                               self.excel['search_field'],
                                               search_word)

            # 空值
            search_word = "  "
            self.server_oper.check_search_null(MobileBy.IOS_CLASS_CHAIN,
                                               self.excel['search_field'],
                                               search_word)

            # 屏蔽词
            search_word = "中国"
            self.server_oper.check_search_null(MobileBy.IOS_CLASS_CHAIN,
                                               self.excel['search_field'],
                                               search_word)

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_003(self):
        "首页金刚区-热门功能-找电话，校验 搜索结果包含搜索关键词「百、度」"
        self.log.info(self.test_sy_jgq_search_phone_003.__doc__)
        try:
            search_word = "百度"
            # 搜索
            self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                self.excel['search_field'], search_word)
            for i in range(0, 5):
                company_name = self.operation.new_element(
                    MobileBy.IOS_CLASS_CHAIN,
                    self.excel['search_phone_company'].format(i + 1)).text
                self.log.info("当前校验的公司名：{}".format(company_name))
                assert search_word[0] in company_name or search_word[
                    1] in company_name, "当前校验的公司名：{}，不包含{}、{}".format(
                    company_name, search_word[0], search_word[1])

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_004(self):
        "首页金刚区-热门功能-找电话，校验 「一键清除」按钮"
        self.log.info(self.test_sy_jgq_search_phone_004.__doc__)
        try:
            search_word = "百度"
            # 搜索
            self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                self.excel['search_field'], search_word)
            # 一键清除
            self.preprocessing.clear_text()
            find_field = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN, self.excel['search_field']).text
            diff_field = "请输入企业名称"
            self.assertEqual(diff_field, find_field,
                             "预期值：{}，实际值：{}".format(diff_field, find_field))

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_005(self):
        "首页金刚区-热门功能-找电话，校验 「清空」按钮-确定功能"
        self.log.info(self.test_sy_jgq_search_phone_005.__doc__)
        try:
            flag = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "清空")
            if not flag:
                self.log.info("没有搜索记录")
                # 搜索
                self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                    self.excel['search_field'], "百度")
                # 一键清除
                self.preprocessing.clear_text()
            self.preprocessing.clear_history()
            elem = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "热门搜索")
            self.assertTrue(elem, "最近搜索没有清除")

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_006(self):
        "首页金刚区-热门功能-找电话，校验 「清空」按钮-取消功能"
        self.log.info(self.test_sy_jgq_search_phone_006.__doc__)
        try:
            flag = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "清空")
            if not flag:
                self.log.info("没有搜索记录")
                # 搜索
                self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                    self.excel['search_field'], "百度")
                # 一键清除
                self.preprocessing.clear_text()
            self.preprocessing.clear_history(select=False)
            elem = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            self.assertTrue(elem, "最近搜索栏不存在")

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_search_phone_007(self):
        "首页金刚区-热门功能-找电话，校验 每个字段内容"
        self.log.info(self.test_sy_jgq_search_phone_006.__doc__)
        try:
            company_name = "北京京东世纪贸易有限公司"
            self.operation.send(MobileBy.IOS_CLASS_CHAIN, self.excel['search_field'], company_name)
            search_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     self.excel['search_phone_company'].format(1)).text
            self.assertEqual(company_name, search_name, "预期值：{}，实际值：{}".format(company_name, search_name))

            company_status = "开业"
            search_status = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                       self.excel['search_company_status'].format(1)).text
            self.assertEqual(company_status, search_status, "预期值：{}，实际值：{}".format(company_status, search_status))

            company_person = "徐雷"
            search_person = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                       self.excel["search_company_person"].format(1)).text
            self.assertEqual(company_person, search_person, "预期值：{}，实际值：{}".format(company_person, search_person))

            company_capital = "139798.56万美元"
            search_capital = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                        self.excel["search_company_capital"].format(1)).text
            self.assertEqual(company_capital, search_capital, "预期值：{}，实际值：{}".format(company_capital, search_capital))

            company_data = "2007-04-20"
            search_data = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     self.excel["search_company_data"].format(1)).text
            self.assertEqual(company_data, search_data, "预期值：{}，实际值：{}".format(company_data, search_data))

            company_tel = "电话:010-89118888更多号码"
            search_tel = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                    self.excel["search_company_tel"].format(1)).text
            self.assertEqual(company_tel, search_tel, "预期值：{}，实际值：{}".format(company_tel, search_tel))

            company_adders = "北京市北京经济技术开发区科创十一街18号C座2层201室"
            search_adders = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                       self.excel["search_company_adders"].format(1)).text
            self.assertEqual(company_adders, search_adders, "预期值：{}，实际值：{}".format(company_adders, search_adders))

            company_navigate = "导航"
            search_navigate = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                       self.excel["search_company_navigate"].format(1)).text
            self.assertEqual(company_navigate, search_navigate, "预期值：{}，实际值：{}".format(company_navigate, search_navigate))

        except AssertionError as ae:
            self.log.error(error_format(ae))
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e


if __name__ == '__main__':
    unittest.main()

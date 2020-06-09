# -*- coding: utf-8 -*-
# @Time    : 2020-04-20 14:29
# @Author  : ZYF
# @File    : test_search_boss.py
import random
import unittest

from appium.webdriver.common.mobileby import MobileBy
from providers.account.account import Account
from providers.common.base_client import BaseClick
from providers.common.base_operation import *

class Test_Search_Boss(BaseClick):
    """查老板"""
    def search_input(self, value):
        """
        查老板搜索中间页搜索框搜索
        value -- 搜索关键字
        """
        search_text = self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入老板信息，如‘马云 杭州’'")
        search_text.send_keys(value)
        # self.operation.send(MobileBy.IOS_PREDICATE, "value == '输入老板信息，如‘马云 杭州’'", value)
        self.log.info("输入关键字 {} 搜索".format(value))
        return value

    def aroundf_boss(self):
        """
        第一次进入身边老板
        @return:
        """
        remind = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "立即开启")
        self.log.info("00000")
        if remind:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "立即开启").click()
            self.log.info("1111")
            # 点击蒙层
        guide = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "OK")
        self.log.info("2222")
        if guide:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "OK").click()
            self.log.info("3333")
    @getimage
    def test_001_CLB_SYSS_p0(self):
        """首页TAB切换"""
        self.log.info(self.test_001_CLB_SYSS_p0.__doc__)
        try:
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            # 断言-tab切换后文本输入框内容不一致

        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_002_CLB_SYSS_p0(self):
        """首页-查老板点击热门搜索"""
        self.log.info(self.test_002_CLB_SYSS_p0.__doc__)
        try:
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            people = self.operation.new_elements(
                MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[2]/XCUIElementTypeButton/XCUIElementTypeStaticText")
            # print('------------',people)
            # print('============', len(people))
            # 首页随机点击老板热搜
            index = random.randint(0, 7)
            p_name = people[index].text
            self.log.info("查老板点击热搜:{}".format(p_name))
            # 进入公司详情页
            people[index].click()
            p_name1 = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.log.info("人员详情页老板名称:{}".format(p_name1))
            # 断言 热搜人员-人员详情页人员
            self.assertEqual(p_name, p_name1)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_003_CLB_SYSS_p0(self):
        """首页-查老板跳转搜索中间页"""
        self.log.info(self.test_003_CLB_SYSS_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 查老板搜索中间页内容
            search_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.log.info("查老板搜索中间页文本内容:{}".format(search_text))
            # 断言-获取到的文本框和的内容是否有符合预期
            self.assertEqual(search_text, "输入老板信息，如‘马云 杭州’")
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_004_CLB_SYZJY_p0(self):
        """查老板搜索中间页点击热门搜索&XX热门老板"""
        self.log.info(self.test_004_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 查老板搜索中间页内容
            search_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            people = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                                 "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeStaticText")
            # print("------",people)
            # print("======",len(people))
            # 中间页随机点击热搜人员
            index = random.randint(0, 8)
            people_n = people[index].text
            people[index].click()
            self.log.info("中间页随机点击热搜人员:{}".format(people_n))
            # 通过中间页热搜进入人详情
            p_name1 = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN,
                "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.log.info("人员详情页老板名称:{}".format(p_name1))
            # 断言 people_n, p_name1 一致
            self.assertEqual(people_n, p_name1)
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 收起键盘
            # self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "search").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/**/XCUIElementTypeTextField[1]").send_keys("\n")

            # 搜索中间页点击热门老板
            hot_people = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]")
            # print("---",hot_people)
            # print(len(hot_people))
            index = random.randint(0, len(hot_people)-1)
            hot_people1 = hot_people[index].text
            hot_people[index].click()
            self.log.info("中间页随机点击热门老板:{}".format(hot_people1))
            # 通过中间页热搜进入人详情-调起登录
            name =  self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '短信验证码登录'")
            self.assertIsNotNone(name)
            # 后退-滑屏 退回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.mobile_swipe("right")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_005_CLB_SYZJY_p0(self):
        """搜索-通过中文人名-有结果"""
        self.log.info(self.test_005_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            name = self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name1 = name_result.text
            # 断言 搜索关键字&搜索结果
            self.assertEqual(name, name1)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(e)
            raise Exception

    @getimage
    def test_006_CLB_SYZJY_p0(self):
        """搜索-通过中文人名-无结果"""
        self.log.info(self.test_006_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索无结果-张三丰安利
            name = self.search_input("张三丰安利")
            # 获取搜索结果列表页无数据的标识
            no_result = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '抱歉，没有找到相关老板！'")
            self.assertIsNotNone(no_result)
            # 查老板无结果
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]")
            boss_no_result = name_result.text
            self.log.info("查老板 {} 无结果，列表结果页展示: {}".format(name, boss_no_result))
            # 查老板无结果-试试查公司
            name_result.click()
            # 查公司输入框文本展示
            search_value = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                      "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.log.info("查公司:{}".format(search_value))
            # 查老板关键词 - 查公司关键词 对应
            self.assertEqual(search_value, name)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_007_CLB_SYZJY_p0(self):
        """搜索-通过英文人名-有结果"""
        self.log.info(self.test_007_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            name = self.search_input("Tom")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name1 = name_result.text
            # 断言 搜索关键字&搜索结果
            self.assertEqual(name, name1)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_008_CLB_SYZJY_p0(self):
        """"搜索-通过英文人名-无结果"""
        self.log.info(self.test_008_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名英文搜索无结果-assert
            name = self.search_input("assert")
            # 获取搜索结果列表页无数据的标识
            no_result = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '抱歉，没有找到相关老板！'")
            self.assertIsNotNone(no_result)
            # 查老板无结果
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]")
            boss_no_result = name_result.text
            self.log.info("查老板 {} 无结果，列表结果页展示: {}".format(name, boss_no_result))
            # 查老板无结果-试试查公司
            name_result.click()
            # 查公司输入框文本展示
            search_value = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                      "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.log.info("查公司:{}".format(search_value))
            # 查老板关键词 - 查公司关键词 对应
            self.assertEqual(search_value, name)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_009_CLB_SYZJY_p0(self):
        """搜索-通过特殊字符-无结果"""
        self.log.info(self.test_009_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 特殊字符搜索无结果-#@$
            name = self.search_input("#@$")

            # 获取搜索结果列表页无数据的标识
            no_result = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '抱歉，没有找到相关老板！'")
            self.assertIsNotNone(no_result)
            # 查老板无结果
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]")
            boss_no_result = name_result.text
            self.log.info("查老板 {} 无结果，列表结果页展示: {}".format(name, boss_no_result))
            # 查老板无结果-试试查公司
            name_result.click()
            # 查公司输入框文本展示
            search_value = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                      "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.log.info("查公司:{}".format(search_value))
            # 查老板关键词 - 查公司关键词 对应
            self.assertEqual(search_value, name)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(e)
            raise Exception

    @getimage
    def test_010_CLB_SYZJY_p0(self):
        """搜索-不输入关键字搜索"""
        self.log.info(self.test_010_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 无关键字搜索-收起键盘
            self.search_input("")
            search = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'Search'")
            search.click()
            search1 = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'Search'")
            self.assertIsNone(search1)
            # 回退首页（页面上无回退按钮-点击取消）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_011_CLB_SYTGY_p0(self):
        """搜索中间页输入框-一键清除"""
        self.log.info(self.test_011_CLB_SYTGY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 搜索中间页输入框点击「一键清除」
            # TODO 一键清除
            time.sleep(2)
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/**/XCUIElementTypeImage/XCUIElementTypeTextField/XCUIElementTypeButton").click()
            # self.preprocessing.clear_text()
            self.log.info("输入框一键清除完成")
            # 查看搜索框文本展示
            name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                              "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.assertEqual(name, "输入老板信息，如‘马云 杭州’")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_012_CLB_SYJGY_p0(self):
        """搜索结果页-筛选"""
        self.log.info(self.test_012_CLB_SYJGY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 地区筛选
            screening = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]")
            screening_befor = screening.text
            self.log.info("默认筛选条件：{}".format(screening_befor))
            screening.click()
            # 一级筛选
            screening1 = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                        "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[1]/XCUIElementTypeCell")
            print('------',len(screening1))

            # index = random.randint(0, len(screening1) - 1)
            index = random.randint(1, 11)
            screening1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[1]/XCUIElementTypeCell[{}]/XCUIElementTypeStaticText".format(index))
            screening_1 = screening1.text
            self.log.info("一级筛选:{}".format(screening_1))
            screening1.click()
            # 二级筛选
            screening2 = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                        "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable[2]/XCUIElementTypeCell/XCUIElementTypeStaticText")
            print('++++++', len(screening2))
            index2 = random.randint(0, len(screening2) - 1)
            screening2 = screening2[index2]
            screening_2 = screening2.text
            self.log.info("二级筛选:{}".format(screening_2))
            screening2.click()
            screening_after = screening.text
            self.assertEqual(screening_2, screening_after)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_013_CLB_SYJGY_p0(self):
        """搜索结果页跳转人详情-未登录"""
        self.log.info(self.test_013_CLB_SYJGY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            name = self.search_input("Tom")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            name = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '短信验证码登录'")
            self.assertIsNotNone(name)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_014_CLB_SYJGY_p0(self):
        """搜索结果页跳转人详情-登录"""
        self.log.info(self.test_014_CLB_SYJGY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            name = self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 获取人员详情页的人员名称
            name1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.log.info("人员详情页名称:{}".format(name1))
            self.assertEqual(name, name1)
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_015_CLB_SYZJY_p0(self):
        """
        搜索中间页点击-发现通讯录中的老板
        通讯录无老板
        """
        self.log.info(self.test_015_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 点击「立即查看」
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '立即查看'").click()
            # 首次进入身边老板提示
            self.aroundf_boss()

            # remind = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "立即开启")
            # self.log.info("00000")
            # if remind:
            #     self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "立即开启").click()
            #     self.log.info("1111")
            # # 点击蒙层
            # guide = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "OK")
            # self.log.info("2222")
            # if guide:
            #     self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "OK").click()
            #     self.log.info("3333")

            # 页面跳转后获取到页面title
            title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeStaticText").text
            self.log.info("页面title展示:{}".format(title))
            self.assertEqual(title, "身边老板")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 回退首页（页面上无回退按钮-点击取消）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_016_CLB_SYZJY_p0(self):
        """搜索中间页最近搜索的功能-最多10条记录"""
        self.log.info(self.test_016_CLB_SYZJY_p0.__doc__)
        try:
            pass
            name_list = [
                "马云",
                "孙凯",
                "王四会",
                "马丁",
                "韩磊",
                "李明",
                "向小叶",
                "蓝小凯",
                "李晓凯",
                "朱小凯",
                "赵小凯",
                "陈小凯",
            ]
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()

            i = 0
            for i in range(len(name_list)):
                self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                    "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage[1]/XCUIElementTypeTextField",
                                    name_list[i])
                self.log.info("输入搜索词：{}".format(name_list[i]))
                # todo 查老板搜索中间页搜索框一键清除
                # self.new_find_element(By.ID, self.ELEMENT["clean_button"]).click()
                i += 1
            print("搜索{}次".format(i))
            history_words = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                                        "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther")
            value = len(history_words)
            for i in range(10):
                self.log.info(
                    "历史:{} vs 输入:{}".format(history_words[i].text, name_list[11 - i])
                )
                self.assertEqual(history_words[i].text, name_list[11 - i], "名字顺序不一致")
            print("页面展示最近搜索记录%s次" % value)
            self.assertEqual(10, value, "搜索12次目前展示{}个最近搜索".format(value))
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_017_CLB_SYZJY_p0(self):
        """搜索中间页最近浏览的功能-最多10条记录"""
        self.log.info(self.test_017_CLB_SYZJY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            name_list = [
                "马云",
                "孙凯",
                "王四会",
                "马丁",
                "韩磊",
                "李明",
                "向小叶",
                "蓝小凯",
                "李晓凯",
                "朱小凯",
                "赵小凯",
                "陈小凯",
            ]
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            i = 0
            for i in range(len(name_list)):
                self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                    "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage[1]/XCUIElementTypeTextField",
                                    name_list[i])
                self.log.info("输入搜索词：{}".format(name_list[i]))

                # 获取搜索结果列表页匹配度最高的第一个
                name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                         "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
                name_result.click()
                # 获取人员详情页的人员名称
                name1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                   "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
                self.log.info("人员详情页名称:{}".format(name1))
                # 退回到搜索中间页
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
                # 搜索中间页输入框一键清除 todo

                i += 1
            print("搜索{}次".format(i))
            history_words = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                                        "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell")

            value = len(history_words)
            for i in range(1,11):
                history_words1 = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN,
                                                            "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{}]/XCUIElementTypeOther/XCUIElementTypeStaticText[1]".format())
                self.log.info(
                    "历史:{} vs 输入:{}".format(history_words1.text, name_list[11 - i])
                )
                self.assertEqual(history_words1.text, name_list[11 - i], "名字顺序不一致")
            print("页面展示最近搜索记录{}次".format(value))
            self.assertEqual(10, value, "搜索12次目前展示{}个最近搜索".format(value))
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_018_CLB_SYZJY_p0(self):
        """最近搜索-一键清除按钮-确认"""
        self.log.info(self.test_018_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 输入关键字搜索-"刘峰"
            self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage[1]/XCUIElementTypeTextField",
                                "刘峰")
            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            #
            Recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            if Recent_search:
                self.log.info("最近搜索-一键清除-确定")
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "清空")[0].click()
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "确定")[0].click()
                Recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            self.assertFalse(Recent_search)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_019_CLB_SYZJY_p0(self):
        """最近搜索-一键清除按钮-取消"""
        self.log.info(self.test_019_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 输入关键字搜索-"刘峰"
            self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage[1]/XCUIElementTypeTextField",
                                "刘峰")
            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            Recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            if Recent_search:
                self.log.info("最近搜索-一键清除-取消")
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "清空")[0].click()
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "取消")[0].click()
                Recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            self.assertTrue(Recent_search)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_020_CLB_SYZJY_p0(self):
        """最近浏览-一键清除按钮-确认"""
        self.log.info(self.test_020_CLB_SYZJY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            if recent_search:
                self.log.info("最近搜索-一键清除-确定")
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "清空")[0].click()
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "确定")[0].click()
                recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            self.assertFalse(recent_search)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_021_CLB_SYZJY_p0(self):
        """最近浏览-一键清除按钮-取消"""
        self.log.info(self.test_021_CLB_SYZJY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            if recent_search:
                self.log.info("最近搜索-一键清除-取消")
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "清空")[0].click()
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "取消")[0].click()
                recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            self.assertTrue(recent_search)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_022_CLB_SYZJY_p0(self):
        """搜索中间页-点击最近搜索"""
        self.log.info(self.test_022_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 输入关键字搜索-"刘峰"
            self.operation.send(MobileBy.IOS_CLASS_CHAIN,
                                "XCUIElementTypeWindow[1]/**/XCUIElementTypeOther/XCUIElementTypeImage[1]/XCUIElementTypeTextField",
                                "刘峰")
            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            Recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近搜索")
            if Recent_search:
                self.log.info("点击最近搜索")
                Recent_search1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther")
                Recent_search_value = Recent_search1.text
                Recent_search1.click()
                # 搜索结果页输入框关键字
                name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                  "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
                self.assertEqual(Recent_search_value, name)
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_023_CLB_SYZJY_p0(self):
        """搜索中间页-点击最近浏览-登录"""
        self.log.info(self.test_023_CLB_SYZJY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            name = self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            if recent_search:
                self.log.info("点击最近浏览")
                recent_search = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                            "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther")
                recent_search.click()
                # 获取人员详情页的人员名称
                p_name1 = self.operation.new_element(
                    MobileBy.IOS_CLASS_CHAIN,
                    "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
                self.assertEqual(name, p_name1)
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_024_CLB_SYZJY_p0(self):
        """搜索中间页-点击最近浏览-未登录"""
        self.log.info(self.test_024_CLB_SYZJY_p0.__doc__)
        try:
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()

            recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            if recent_search:
                self.log.info("点击最近浏览")
                recent_search = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                           "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther")
                recent_search.click()
                # 通过最近浏览进入人详情-调起登录
                name = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '短信验证码登录'")
                self.assertIsNotNone(name)
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_025_CLB_SYdb_p0(self):
        """
        首页底部-查老板，未登录
        点击热门人物可以查看人详情
        点击热门人物合作伙伴拉起登录
        点击搜索框跳转查老板搜索中间页
        """
        self.log.info(self.test_025_CLB_SYdb_p0.__doc__)
        try:
            # 点击首页底部「查老板」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[2]").click()
            # 点击老板推荐
            name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                              "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name1 = name.text
            self.log.info("点击热搜老板{}".format(name1))
            name.click()
            # 获取人员详情页的人员名称
            p_name1 = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN,
                "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.assertEqual(name1, p_name1)
            # 后退-页面后退首页底部查老板tab页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 点击老板推荐-合作伙伴
            name1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[3]")
            name2 = name1.text
            self.log.info("点击合作伙伴{}".format(name2))
            name1.click()
            # 通过点击合作伙伴-调起登录
            login = self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '短信验证码登录'")
            self.assertIsNotNone(login)
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))

    @getimage
    def test_026_CLB_SYdb_p0(self):
        """
        首页底部-查老板，登录
        点击热门人物可以查看人详情
        点击热门人物合作伙伴拉起登录
        点击搜索框跳转查老板搜索中间页
        """
        self.log.info(self.test_026_CLB_SYdb_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 点击首页底部「查老板」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[2]").click()
            # 点击老板推荐
            name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                              "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name1 = name.text
            self.log.info("点击热搜老板{}".format(name1))
            name.click()
            # 获取人员详情页的人员名称
            p_name1 = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN,
                "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.assertEqual(name1, p_name1)
            # 后退-页面后退首页底部查老板tab页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 点击老板推荐-合作伙伴
            name1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[3]")
            name2 = name1.text
            self.log.info("点击合作伙伴{}".format(name2))
            name1.click()
            # 通过点击合作伙伴-查看详情
            # 获取人员详情页的人员名称
            p_name1 = self.operation.new_element(
                MobileBy.IOS_CLASS_CHAIN,
                "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]").text
            self.assertEqual(name2, p_name1)
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))

    @getimage
    def test_027_CLB_SYdb_p0(self):
        """首页底部-查老板，点击输入框"""
        self.log.info(self.test_026_CLB_SYdb_p0.__doc__)
        try:
            # 点击首页底部「查老板」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[2]").click()
            # 点击页面顶部输入框
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage/XCUIElementTypeButton").click()
            self.log.info("点击输入框页面跳转查老板搜索中间页")
            # 查老板搜索中间页内容
            search_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]/XCUIElementTypeTextField[1]").text
            self.log.info("查老板搜索中间页文本内容:{}".format(search_text))
            self.assertEqual("输入老板信息，如‘马云 杭州’", search_text)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))

    @getimage
    def test_028_CLB_SYZJY_p0(self):
        """最近浏览-点击「X」"""
        self.log.info(self.test_021_CLB_SYZJY_p0.__doc__)
        try:
            account = Account()
            acc_vip_name = account.get_account('vip')
            acc_pwd = account.get_pwd()
            self.log.info("登录VIP账号：{}".format(acc_vip_name))
            self.preprocessing.login(acc_vip_name, acc_pwd)
            # 页面跳转老板搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            # 人名搜索有结果-刘峰
            self.search_input("刘峰")
            # 获取搜索结果列表页匹配度最高的第一个
            name_result = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                     "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]")
            name_result.click()
            # 后退-页面后退搜索中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

            # 搜索中还能页一键清除 ---不能用，采用搜索结果页后退首页再进入以获取最近搜索
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]/XCUIElementTypeStaticText[1]").click()
            recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            if recent_search:
                self.log.info("最近搜索-一键清除-取消")
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "清空")[0].click()
                self.operation.new_elements(MobileBy.ACCESSIBILITY_ID, "取消")[0].click()
                recent_search = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
            self.assertTrue(recent_search)
            # 取消回到首页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 账号使用完还回去
            account.release_account(acc_vip_name, "vip")
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

if __name__ == '__main__':
    unittest.main()

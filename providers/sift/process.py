# -*- coding: utf-8 -*-
# @Time    : 2020-05-26 15:47
# @Author  : XU
# @File    : process.py
# @Software: PyCharm
import os
import json
from providers.common.base_operation import Operation
from providers.common.preprocessing import Preprocessing
from appium.webdriver.common.mobileby import MobileBy
from providers.sift.operation import SiftOperation


class SiftProcess:

    def __init__(self, driver):
        self.driver = driver
        # 获取基础操作
        self.operation = Operation(driver)
        self.preprocessing = Preprocessing(driver)
        sift_operate = SiftOperation(driver)
        self.elements = sift_operate.get_element()

    def random_key(self, key, option):
        """
        更多筛选，选中筛选项
        :param key: 搜索词
        :param option: 筛选项
        :return:
        """
        # 点击首页-查关系tab
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch relation n'").click()
        # 点击输入框
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["search_box"]).click()
        # 点击查关系-开始节点输入框
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '添加第一个公司或老板'").click()
        # 搜索中间页，输入开始节点
        # todo 搜索词做成随机的
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入公司名称、老板姓名、品牌名称等'").send_keys(str(key))
        # 点击更多筛选
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value = '更多筛选'").click()
        # 点击-商标
        # todo 筛选项做成随机的
        self.preprocessing.random_options(find_type=MobileBy.IOS_PREDICATE, find_element="value = '商标'")
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value = '{}'".format(option)).click()
        # 点击-确认
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value = '确认'").click()

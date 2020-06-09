# -*- coding: utf-8 -*-
# @Time    : 2020-05-09 15:39
# @Author  : XU
# @File    : operating.py
# @Software: PyCharm
import os
import json
from providers.common.base_operation import Operation
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
element = BASE_DIR + '/elements.json'


class RelationOperate:
    elements = None

    def __init__(self, driver):
        self.driver = driver
        # 获取基础操作
        self.operation = Operation(driver)

    def get_element(self):
        """获取「查关系」元素"""
        with open(element, 'r', encoding='UTF-8') as f:
            elements = json.load(f)
            self.elements = elements
        return elements

    def hot_relation(self):
        """进入样例关系"""
        # 点击首页-查关系tab
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch relation n'").click()
        # 点击输入框
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["search_box"]).click()
        # 点击马云-赵薇，热门关系
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["hot_relation"]).click()
        relation_point = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '王忠军'")
        return relation_point

# -*- coding: utf-8 -*-
# @Time    : 2020-05-26 15:45
# @Author  : XU
# @File    : operation.py
# @Software: PyCharm
import os
import json
from providers.common.base_operation import Operation
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
element = BASE_DIR + '/elements.json'


class SiftOperation:
    elements = None

    def __init__(self, driver):
        self.driver = driver
        # 获取基础操作
        self.operation = Operation(driver)

    def get_element(self):
        """获取「更多筛选」元素"""
        with open(element, 'r', encoding='UTF-8') as f:
            elements = json.load(f)
            self.elements = elements
        return elements

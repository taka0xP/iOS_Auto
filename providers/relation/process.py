# -*- coding: utf-8 -*-
# @Time    : 2020-05-09 19:27
# @Author  : XU
# @File    : process.py
# @Software: PyCharm
import os
import json
from providers.common.base_operation import Operation
from providers.common.preprocessing import Preprocessing
from appium.webdriver.common.mobileby import MobileBy
from providers.relation.operating import RelationOperate


class RelationProcess:
    def __init__(self, driver):
        self.driver = driver
        # 获取基础操作
        self.operation = Operation(driver)
        self.preprocessing = Preprocessing(driver)
        relation_operate = RelationOperate(driver)
        self.elements = relation_operate.get_element()

    def relation_share(self):
        """更多操作-分享"""
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation plus'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relationShip share'").click()
        share_tag = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '微信'")
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        return share_tag

    def relation_save(self):
        """更多操作-保存"""
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation plus'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relationShip save'").click()
        self.preprocessing.get_permission()
        save_tag = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '已保存相册'")
        return save_tag

    def relation_scan(self):
        """更多操作-扫一扫"""
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation plus'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relationShip scan'").click()
        scan_tag = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.elements["scan"])
        self.preprocessing.backtrack()
        return scan_tag

    def relation_edit(self):
        """更多操作-删减"""
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation plus'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relationShip edit'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '赵薇'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relationShip sure n'").click()
        edit_tag = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '赵薇'")
        return edit_tag

    def relation_demo(self):
        """查关系样例，相关操作"""
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'fullScreen n'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'outFullScreen n'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation clear n'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除所有信息'").click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'company logo'").click()
        home_page_tag = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch relation n'")
        return home_page_tag

    def relation_search(self):
        """输入查关系节点，相关操作"""
        # 点击首页-查关系tab
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch relation n'").click()
        # 点击输入框
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["search_box"]).click()
        # 点击查关系-开始节点输入框
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '添加第一个公司或老板'").click()
        # 搜索中间页，输入开始节点
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入公司名称、老板姓名、品牌名称等'").send_keys("北京金堤科技有限公司")
        # 选中节点1
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["first_port"]).click()
        # 点击查关系-结束节点输入框
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '添加第二个公司或老板'").click()
        # 搜索中间页，输入结束节点
        self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入公司名称、老板姓名、品牌名称等'").send_keys("盐城金堤科技有限公司")
        # 选中节点2
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.elements["first_port"]).click()
        # 节点输入完毕，点击查关系按钮
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'relation discover n'").click()

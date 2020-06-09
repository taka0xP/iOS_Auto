#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Soner
# @version : 1.0.0

import time
from providers.common.base_operation import Operation
from providers.common.preprocessing import Preprocessing
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import Logger, error_format


class ServerOperating():
    def __init__(self, driver, excel, log=None):
        if log is None:
            self.log = Logger("金刚区相关操作").getlog()
        else:
            self.log = log
        self.driver = driver
        self.excel = excel
        self.operation = Operation(driver, log=log)
        self.preprocessing = Preprocessing(driver= driver, log=log)

    def click_all(self):
        """
        点击 「全部」
        @return:
        """
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['all_entrance']).click()

    def click_server(self, server_name):
        # 点击 金刚取-「服务名字」
        self.operation.new_element(MobileBy.ACCESSIBILITY_ID, server_name).click()
        if server_name == "天眼地图":
            # 获取权限
            self.preprocessing.get_permission()
            # 是否有 授权取消按钮
            if self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '取消'"):
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            if self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map']):
                # 点击蒙层
                e1 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map'])
                self.operation.mobile_tap(e1)
                e2 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map'])
                self.operation.mobile_tap(e2)
                e3 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map'])
                self.operation.mobile_tap(e3)
            time.sleep(3)

    def aroundf_boss(self):
        """
        第一次进入身边老板
        @return:
        """
        remind = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, self.excel['open_now'])
        if remind:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, self.excel['open_now']).click()
            # 点击蒙层
            guide = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, self.excel['follow_guide'])
            if guide:
                self.operation.new_element(MobileBy.ACCESSIBILITY_ID, self.excel['follow_guide']).click()

    def get_titile(self, tl=2):
        """
        获取金刚区页面title
        @return:
        """
        time.sleep(tl)
        find_title = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['title_text']).text
        self.log.info("获取到的页面title：{}".format(find_title))
        return find_title

    def get_text_field(self):
        """
        获取 输入框预留文案
        @return:
        """
        text_field = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_field']).text
        self.log.info("获取到的预留文案：{}".format(text_field))
        return text_field

    def check_title(self, server_name, diff_con, tl=2):
        """
        校验 titile
        @param server_name:
        @param diff_con:
        @param tl:
        @return:
        """
        self.click_server(server_name)
        diff_title = diff_con
        if server_name == "身边老板":
            self.aroundf_boss()
        find_title = self.get_titile(tl=tl)
        assert diff_title == find_title, "预期值：{}，实际值：{}".format(diff_title, find_title)

    def check_text_field(self, server_name, diff_con):
        """
        校验 搜索框预留文案
        @param server_name:
        @param diff_con:
        @return:
        """
        diff_content = diff_con
        self.click_server(server_name)
        find_content = self.get_text_field()
        assert diff_content == find_content, "预期值：{}，实际值：{}".format(diff_content, find_content)

    def check_search_null(self, find_type, find_element, content):
        """
        校验搜索结果为空
        @param find_type:
        @param find_element:
        @param content:
        @return:
        """
        self.operation.send(find_type=find_type, find_element=find_element, content=content)
        flag = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "空列表")
        assert flag, "搜索值：{}，有实际结果".format(content)
        self.preprocessing.clear_text()

    def vip_popup(self, msg):
        """
        校验vip 弹窗
        @param msg:
        @return:
        """
        vip_title = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, msg)
        assert vip_title is True, "预期值：{} 不存在".format(msg)
        # 点击「关闭」
        self.operation.new_element(MobileBy.ACCESSIBILITY_ID, self.excel['vip_close']).click()

    def check_vip_popup(self, find_type, find_element, item_num, msg="VIP会员可使用高级筛选条件"):
        """
        校验一组类型VIP 弹窗
        @param find_type:
        @param find_element:
        @param iterm_num:
        @param msg:
        @return:
        """
        mores = self.operation.new_elements(find_type, find_element.format(item_num))
        for index in range(len(mores)):
            if index == 0:
                self.log.info("待校验的VIP筛选条件：{}".format(mores[index].text))
                mores[index].click()
            else:
                new_mores = self.operation.new_elements(find_type, find_element.format(item_num))
                self.log.info("待校验的VIP筛选条件：{}".format(new_mores[index].text))
                new_mores[index].click()
            self.vip_popup(msg=msg)

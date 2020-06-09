#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7
# @Author  : Soner
# @version : 1.0.0

import random
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from providers.common.base_operation import Operation
from providers.common.logger import Logger, error_format
from providers.common.read_data import ReadExcel


class Preprocessing():
    def __init__(self, driver, log=None):
        if log is None:
            self.log = Logger("预处理步骤").getlog()
        else:
            self.log = log
        self.driver = driver
        self.excel = ReadExcel().read_excel("common")
        self.operation = Operation(driver, self.log)
        self.by = MobileBy()

    def skip_guide(self, number=4):
        """
        跳过引导页
        @param number:
        @return:
        """
        try:
            for i in range(number):
                self.operation.mobile_swipe('left')
            self.log.info("跳过首页引导")
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def agree_license(self):
        """
        点击用户协议
        @return:
        """
        try:
            element = self.operation.is_element(self.by.IOS_PREDICATE, self.excel['agree_license'])
            if element:
                self.operation.new_element(self.by.IOS_PREDICATE, self.excel['agree_license']).click()
                self.log.info("点击同意用户协议")
        except Exception as e:
            self.log.error('点击同意用户协议失败！！！')
            self.log.error(error_format(e))
            raise e

    def cancel_update(self):
        """
        跳过 升级弹窗
        @return:
        """
        try:
            element = self.operation.is_element(self.by.IOS_PREDICATE, self.excel['update_title'], outtime=10)
            if element:
                self.operation.new_element(self.by.IOS_PREDICATE, self.excel['close_update']).click()
                self.log.info("跳过升级弹窗")
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def skip_monitor(self):
        """
        跳过监控日报
        @return:
        """
        try:
            element = self.operation.is_element(self.by.IOS_PREDICATE, self.excel['monitor_title'])
            if element:
                self.operation.new_element(self.by.IOS_PREDICATE, self.excel['close_monitor']).click()
                self.log.info("跳过监控日报")
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def skip_monitor_daily_email(self, select=False, email=None):
        """
        监控日报相关操作
        @param select:
        @param email:
        @return:
        """
        if self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                      "XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]"):
            if select:
                if email:
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").click()
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                               "XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").send_keys(
                        email)
                self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "保存").click()
            else:
                self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "跳过").click()

    def back_index(self):
        """
        回到首页
        @return:
        """
        back_count = 0
        while back_count < 10:
            back_count += 1
            flag = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(1), outtime=1)
            if flag:
                self.log.info("已返回到首页")
                break
            else:
                self.log.info("未返回到首页，点击「返回」按钮")
                self.backtrack()

    def backtrack(self):
        """
        返回
        @return:
        """
        elements = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['button'])
        for element in elements:
            if element.get_attribute("visible") == "true" and element.get_attribute('name') in ['nav back new',
                                                                                                'App Back']:
                element.click()
                break

    def hide_keyboard(self):
        """
        隐藏键盘 + 搜索 按钮功能
        @return:
        """
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_bar']).send_keys("\n")

    def clear_text(self):
        """
        一键清除 按钮
        @return:
        """
        self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "清除文本").click()

    def clear_history(self, select=True):
        """
        历史 「清空」按钮
        @return:
        """
        self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "清空").click()
        if select:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "确定").click()
        else:
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "取消").click()

    def get_permission(self):
        """
        获取 所有权限
        @return:
        """
        permission = self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['permission'], outtime=2)
        if permission is not None:
            permission.click()
            self.log.info("获取权限")

    def is_login(self):
        """
        判断 登陆状态
        @return:
        """
        # 回到首页
        self.back_index()
        # 进入 我的
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(5)).click()
        # 是否有 登陆 按钮
        login_status = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "立即登录", outtime=3)
        if login_status:
            self.log.info("未登录账号")
            result = not login_status
        else:
            self.log.info("已登录账号")
            result = not login_status
        return result

    def login(self, phone_num, password):
        """"
        登录公用方法
         @return:
        """
        try:
            flag = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '密码登录'")
            if flag:
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '密码登录'").click()
                phone = self.operation.is_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'")
                if phone:
                    self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'").click()
                else:
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_phone']).click()
                    self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'").send_keys(phone_num)
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入密码'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入密码'").send_keys(password)
                self.hide_keyboard()
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['agreement_button']).click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '登录'").click()
                element = self.operation.is_element(self.by.IOS_PREDICATE, self.excel['monitor_title'])
                if element:
                    self.operation.new_element(self.by.IOS_PREDICATE, self.excel['close_monitor']).click()
                    self.log.info("跳过监控日报")
            else:
                self.back_index()
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['mytab_button']).click()
                self.operation.mobile_swipe('down')
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '立即登录'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '密码登录'").click()
                phone = self.operation.is_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'")
                if phone:
                    self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'").click()
                else:
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['login_phone']).click()
                    self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入手机号'").send_keys(phone_num)
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入密码'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入密码'").send_keys(password)
                self.hide_keyboard()
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['agreement_button']).click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '登录'").click()

                element = self.operation.is_element(self.by.IOS_PREDICATE, self.excel['monitor_title'])
                if element:
                    self.operation.new_element(self.by.IOS_PREDICATE, self.excel['close_monitor']).click()
                    self.log.info("跳过监控日报")
                login_status = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '立即登录'")
                if login_status is not True:
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(1)).click()
                    self.log.info("登录成功，并回到首页")
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def logout(self):
        """
        退出登录
        @return:
        """
        flag = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(1))
        if flag is not True:
            self.back_index()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(5)).click()
        login_status = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '立即登录'")
        if login_status:
            self.log.info("已经是未登录状态")
        else:
            swip_up_count = 0
            while swip_up_count < 4:
                swip_up_count += 1
                elment = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '设置'")
                if elment:
                    self.log.info("找到设置按钮")
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['set_icon']).click()
                    break
                else:
                    self.log.info("未找到设置按钮，继续向上滑")
                    self.operation.mobile_swipe('up')
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '退出'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '确定'").click()
            swip_down_count = 0
            while swip_down_count < 4:
                swip_down_count += 1
                log_stu = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '立即登录'")
                if log_stu:
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(1)).click()
                    self.log.info("已退出登录并回到首页")
                    break
                else:
                    self.log.info("未找到立即登录按钮，继续向上滑")
                    self.operation.mobile_swipe('down')

    def enter_monitor_list(self):
        """
        进入到 我的->监控列表
        @return:
        """
        # 返回到「首页」
        try:
            self.back_index()
            # 点击「我的」
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['index'].format(5)).click()
            # 点击「我的监控」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, '我的监控').click()
            # 点击「监控列表」
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, '监控列表').click()
        except Exception as e:
            self.log.error(error_format(e))

    def random_options(self, find_type, find_element, num=None, x=0.03, fromy=0.6, toy=0.5):
        """
        随机查找一个选项
        @param find_type:  查找方法
        @param find_element:  查找元素
        @param num: 指定第几个筛选项，默认为None，随机选择
        @param x: 滑动 x 起始/结束坐标
        @param fromy: 滑动 y 起始坐标
        @param toy:  滑动 y 结束坐标
        @return: 会返回选择项的文本名字
        """
        groups = self.operation.new_elements(find_type=find_type, find_element=find_element)
        groups_len = len(groups)
        if not num is None:
            random_num = num - 1
        else:
            random_num = random.randint(0, groups_len - 1)
        self.log.info("随机项下标：{}".format(random_num))
        random_name = groups[random_num].text
        self.log.info("共有 {} 选项，选择第 {} 个：{}".format(groups_len, random_num + 1, random_name))
        loop_num = 5
        while loop_num > 0:
            if loop_num == 5:
                find_groups = groups
            else:
                find_groups = self.operation.new_elements(find_type=find_type, find_element=find_element)
            self.log.info("选项是否可见：{}".format(find_groups[random_num].get_attribute("visible")))

            if find_groups[random_num].get_attribute("visible") == "true":
                if find_groups[random_num].text == random_name:
                    find_groups[random_num].click()
                    return random_name
                else:
                    raise NoSuchElementException("随机的选项：{}，实际要点击的选项：{}".format(random_name,
                                                                 find_groups[random_num].text))
            self.operation.mobile_drag_to_duration(fromX=x, fromY=fromy, toX=x, toY=toy)
            loop_num -= 1
        else:
            raise NoSuchElementException("随机项：{} 未找到".format(random_name))

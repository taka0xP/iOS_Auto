#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7
# @Author  : Soner
# @version : 1.0.0

import time
import os
import re
from functools import wraps
from selenium.webdriver.support.wait import WebDriverWait
from providers.common.logger import Logger, error_format


class Operation():
    def __init__(self, driver, log=None):
        self.driver = driver
        if log is None:
            self.log = Logger("基础操作").getlog()
        else:
            self.log = log

    def _re_count(self, count_text):
        """
        正则匹配文本中的数字
        @param count_text:
        @return:
        """
        try:
            match = re.search(r"([0-9]\d*)", count_text).group()
            return int(match)
        except AttributeError as ae:
            self.log.info("没有匹配到数字")
            raise ae
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def mobile_swipe(self, direction):
        """
        在指定的屏幕上的控件或App的控件上执行“滑动”操作，一般是针对整个屏幕。这个方法不支持通过坐标来操作，
        并且仅仅是简单的模拟单个手指滑动。这个方法对于诸如相册分页、切换视图等情况可能会发挥比较大的作用
        @param direction: left, right, up, down
        @return:
        """
        self.driver.execute_script('mobile: swipe', {'direction': direction})

    def mobile_scroll(self, direction):
        """
        滑动整屏
        @param direction: ‘up’, ‘down’, ‘left’ or ‘right’. 该参数与swipe中的比，差别在于scroll会尝试将当前界面完全移动到下一页
        @return:
        mobile：scroll;该方法在实际使用调用时，会滚动2次。执行时间很长
        """
        self.driver.execute_script('mobile:scroll',{"direction":direction})

    def mobile_pinch(self, element, scale, velocity=1.1):
        """
        在给定的控件或应用程序控件上执行捏合手势
        @param element: 需要捏合的控件ID。如果没有提供该参数的话，则会使用App的控件作为替代
        @param scale: 浮动型夹点尺度。使用0和1之间的比例来“捏紧”或缩小，大于1的比例“撑开”或放大
        @param velocity: 每秒缩放速度（浮点值）
        @return:
        """
        self.driver.execute_script('mobile:pinch', {'element': element, 'scale': scale, 'velocity': velocity})

    def mobile_tap(self, element=None, x=0, y=0):
        """
        在指定控件或屏幕上的坐标执行点击手势
        @param element:  如果设置了element参数，则x、y代表的是以当前element为边界的xy轴。若未设置，则x,y代表的是以手机屏幕为边界
        @param x:
        @param y:
        @return:
        """
        time.sleep(1)
        if element is None:
            self.driver.execute_script('mobile:tap', {"x": x, "y": y})
        else:
            self.driver.execute_script('mobile:tap', {"element":element, "x": x, "y": y})

    def mobile_double_tap(self, element=None, x=0, y=0):
        """
        在指定控件上或屏幕上执行双击手势
        @param element:  需要双击的控件ID
        @param x: 屏幕x轴坐标点，浮点型. 仅当element未设置时才是强制参数
        @param y: 屏幕y轴坐标点，浮点型. 仅当element未设置时才是强制参数
        @return:
        """
        if element is None:
            self.driver.execute_script("mobile:doubleTap", {"x":x, "y":y})
        else:
            self.driver.execute_script("mobile:doubleTap", {"element":element, "x":x, "y":y})

    def mobile_touch_hole(self, element=None, duration=2.0, x=0, y=0):
        """
        在指定控件上或屏幕上长按的手势操作
        @param element: 需要长按的控件ID
        @param duration: 长按的持续时间（秒）,浮点型
        @param x: 屏幕x轴坐标点，浮点型. 仅当element未设置时才是强制参数
        @param y: 屏幕y轴坐标点，浮点型. 仅当element未设置时才是强制参数
        @return:
        """
        if element is None:
            self.driver.execute_script("mobile:touchAndHole", {"x":x, "y":y, "duration": duration})
        else:
            self.driver.execute_script("mobile:touchAndHole", {"element":element, "duration": duration})

    def mobile_two_finger_tap(self, element):
        """
        在给定元素或应用程序元素上执行两个手指点击手势
        @param element:
        @return:
        """
        self.driver.execute_script("mobile:twoFingerTap", {"element":element})

    def mobile_drag_to_duration(self, fromX, fromY, toX, toY, duration=0.5, element=None, ):
        """
        通过坐标点执行拖放手势。可以在控件上执行，也可以在屏幕上执行
        @param duration: 开始拖动点之前的点击手势需要多长时间才能开始拖动
        @param element: 控件ID，可以指定为None，为None时以整个手机屏幕为边界, 如果滑动中起点坐标在控件上，会触发点击操作
        @param fromX: 起点X坐标
        @param fromY: 起点Y坐标
        @param toX: 终点X坐标
        @param toY: 终点Y坐标
        @return:
        """
        width, height = self.get_size()
        self.log.info("起点X、Y坐标:({},{})、终点X、Y坐标：({},{})".format(width * fromX, height * fromY, height * toX, width * toY))
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": duration, "element": element, "fromX": width * fromX,
                                    "fromY": height * fromY, "toX": width * toX,
                                    "toY": height * toY})

    def mobile_alert(self, action, button_label):
        """
        对弹窗执行操作
        @param action: accept, dismiss, getButtons
        @param button_label:
        @return:
        """
        self.driver.execute_script("mobile:alert", {"action": action, "buttonLabel": button_label})

    def is_element(self, find_type, find_element, outtime=5):
        """
        判断元素是否存在
        @param loc:
        @param outtime:
        @return:
        """
        element = self.new_element(find_type, find_element, outtime=outtime)
        if element:
            return True
        else:
            return False

    def new_element(self, find_type, find_element, outtime=10):
        """
        查找元素
        @param loc:
        @param outtime:
        @return:
        """
        try:
            element = WebDriverWait(self.driver, outtime, 0.01).until(
                lambda driver: driver.find_element(by=find_type, value=find_element)
            )
            return element
        except Exception as e:
            self.log.error("页面中找不到元素：({}:{})".format(find_type, find_element))
            return None

    def new_elements(self, find_type, find_element, outtime=10):
        """
        查找一组元素
        @param loc:
        @param outtime:
        @return:
        """
        try:
            elements = WebDriverWait(self.driver, outtime, 0.01).until(
                lambda driver: driver.find_elements(by=find_type, value=find_element)
            )
            return elements
        except Exception as e:
            self.log.error("页面中找不到元素：({}:{})".format(find_type, find_element))
            return None

    def repeatedly_element(self, find_type, find_element, re_element, outtime=10):
        """
        当有A/B时，class_chain链式查找方法
        @param find_type:
        @param find_element:
        @param re_element:
        @param outtime:
        @return:
        """
        ele =  self.new_element(find_type, find_element, outtime)
        if ele:
            return ele
        self.log.info("使用第二元素查找")
        re_ele = self.new_element(find_type, re_element, outtime)
        if re_ele:
            return re_ele
        return None

    def repeatedly_elements(self, find_type, find_element, re_element, outtime=10):
        """
        当有A/B时，class_chain链式查找方法
        @param find_type:
        @param find_element:
        @param re_element:
        @param outtime:
        @return:
        """
        ele =  self.new_elements(find_type, find_element, outtime)
        if ele:
            return ele
        self.log.info("使用第二元素查找")
        re_ele = self.new_elements(find_type, re_element, outtime)
        if re_ele:
            return re_ele
        return None

    def get_size(self):
        """
        获取屏幕尺寸
        @return:
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def get_count(self, **kwargs):
        """
        正则匹配文本中的数字，适用于 查找count数
        @param kwargs:
                elements：一个element对象集合，用于批量匹配
                单个匹配必传参数 find_type、find_element
        @return:
        """
        try:
            if kwargs.get('elements'):
                result = list()
                for element in kwargs['elements']:
                    count_num = self._re_count(element)
                    result.append(count_num)
                return result
            else:
                if kwargs.get('find_type') and kwargs.get('find_element'):
                    count_text = self.new_element(kwargs['find_type'], kwargs['find_element']).text
                    return self._re_count(count_text)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    def send(self, find_type, find_element, content):
        """
        输入内容并搜索
        @param find_type:   查找方式
        @param find_element:    查找元素
        @param content: 输入内容
        @return:
        """
        self.new_element(find_type=find_type, find_element=find_element).send_keys(content + "\n")















# 失败截图base64
fail_screenshot = dict()
# 用例执行失败自动获取截图装饰器
def getimage(function):
    global fail_screenshot

    @wraps(function)
    def get_error_image(self, *args, **kwargs):
        try:
            return function(self, *args, **kwargs)
        except:
            time_str = time.strftime("%Y%m%d_%H.%M.%S")
            resultpath = (
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    + "/report/FailureScreenshots/"
            )

            self.driver.get_screenshot_as_file(
                resultpath + time_str + function.__name__ + ".png"
            )
            fail_screenshot.update(
                {function.__name__: self.driver.get_screenshot_as_base64()}
            )
            raise

    return get_error_image

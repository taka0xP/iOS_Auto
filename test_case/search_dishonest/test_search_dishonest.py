#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3
# @Author  : Soner
# @version : 1.0.0


import unittest
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import Logger, error_format
from providers.common.base_operation import getimage
from providers.common.base_client import BaseClick
from providers.common.read_data import ReadExcel

log = Logger("查老赖1").getlog()


class TestSearchDisHonest1(BaseClick):

    def setup(self):
        self.preprocessing.back_index()

    @getimage
    # @unittest.skip("检查输入框内默认的'输入人名/公司名/身份证号码/组织机构代码'")
    def test_SerchDishonest_001(self):
        log.info(self.test_SerchDishonest_001.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            #点击查老赖
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            #校验默认输入框内容
            assert "输入人名/公司名/身份证号码/组织机构代码" == self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").text
            # self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "name == 'deadbeatIcon'").click()
            # 返回
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验2个热点公司，2个热点人员")
    def test_SerchDishonest_002(self):
        log.info(self.test_SerchDishonest_002.__doc__)
        try:
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '全部'").click()
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            #点击查老赖
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            #校验2个热点公司
            assert "" or None != self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]').text
            assert "" or None != self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]').text
            #校验2个热点人员
            assert "" or None != self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]').text
            assert "" or None != self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]').text
            # self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "name == 'deadbeatIcon'").click()
            # 返回
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验查老赖搜索结果页，查看：失信企业，失信自然人")
    def test_SerchDishonest_003(self):
        log.info(self.test_SerchDishonest_003.__doc__)
        try:
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '全部'").click()
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("1234567")
            # 校验两个按钮
            self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "失信企业 0"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "失信自然人 3"').click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验查老赖搜索结果页，点击：2个热点人物、2个热点公司")
    def test_SerchDishonest_004(self):
        log.info(self.test_SerchDishonest_004.__doc__)
        try:
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '全部'").click()
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, 'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]').click()
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "nav back new").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, 'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]').click()
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "nav back new").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]').click()
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "nav back new").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]').click()
            # self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "nav back new").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("搜索内容小于2的文字，校验输入框内容为马，且不跳转搜索（无法抓取到toast弹窗）")
    def test_SerchDishonest_005(self):
        log.info(self.test_SerchDishonest_005.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("马")
            # 校验：搜索框、热门区域仍能点击（无法抓取到toast弹窗）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '马'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("搜索内容小于6的数字，校验输入框内容为12345，且不跳转搜索（无法抓取到toast弹窗）")
    def test_SerchDishonest_006(self):
        log.info(self.test_SerchDishonest_006.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("12345")
            # 校验：搜索框、热门区域仍能点击（无法抓取到toast弹窗）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '12345'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                       'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("清除历史记录")
    def test_SerchDishonest_007(self):
        log.info(self.test_SerchDishonest_007.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("王伟")
            # 校验：搜索框、热门区域仍能点击（无法抓取到toast弹窗）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '王伟'").click()
            # self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "nav back new"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "nav back new"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "输入人名/公司名/身份证号码/组织机构代码"').click()
            #判断清除历史记录存在(当前不存在)
            try:
                self.operation.new_element(MobileBy.IOS_PREDICATE,'name == "beginSearch clear"').click()
                ret = 0
            except:
                ret=1
            assert ret==1
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验标签，人数")
    def test_SerchDishonest_008(self):
        log.info(self.test_SerchDishonest_008.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'value == "输入人名/公司名/身份证号码/组织机构代码"').send_keys("司马朝")
            # 校验：失信自然人 3、搜索到 3 个老赖、失信企业 3
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '失信自然人 3'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '搜索到 3 个老赖'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '失信企业 3'")
            #查看三个人，确定是老赖标签
            assert "老赖"==self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[4]").text
            assert "老赖"==self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeStaticText[4]").text
            assert "老赖"==self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]").text
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("清除历史记录")
    def test_SerchDishonest_009(self):
        log.info(self.test_SerchDishonest_009.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("王伟")
            # 校验：搜索框、热门区域仍能点击（无法抓取到toast弹窗）
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'Search'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '王伟'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'name == "nav back new"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'name == "nav back new"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'name == "输入人名/公司名/身份证号码/组织机构代码"').click()
            # 判断清除历史记录存在(当前存在)
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'name == "beginSearch clear"').click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, 'name == "确定"').click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验失信自然人 999+；搜索到n个老赖,n>999")
    def test_SerchDishonest_010(self):
        log.info(self.test_SerchDishonest_010.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("王伟")
            # 校验：校验失信人999，搜索到>999
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'Search'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '失信自然人 999+'")
            retStr = self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE[cd] '搜索到*'").get_attribute("name")
            assert int(retStr.split(" ")[1])>999
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验身份信息")
    def test_SerchDishonest_011(self):
        log.info(self.test_SerchDishonest_011.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("司马朝")
            # 校验：身份信息，完全匹配第一个人。
            assert "身份证号码：3211811991****3234"==self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[5]").get_attribute("name")
            assert "简介：司马朝，男，1991年出生，江苏省镇江市丹阳市人。"==self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, "XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]").get_attribute("name")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：失信自然人为0时，失信企业3；在失信企业tab中，搜索到3个老赖")
    def test_SerchDishonest_012(self):
        log.info(self.test_SerchDishonest_012.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("暴风北京")
            #校验：失信自然人为0时，失信企业3；在失信企业tab中，搜索到3个老赖
            self.operation.new_element(MobileBy.IOS_PREDICATE,"name LIKE '失信企业*'")
            self.operation.new_element(MobileBy.IOS_PREDICATE,"name LIKE '搜索到 * 个老赖'")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：暴风北京搜索结果")
    def test_SerchDishonest_013(self):
        log.info(self.test_SerchDishonest_013.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("暴风北京")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信企业*'").click()
            # 校验：失信自然人为0时，失信企业3；在失信企业tab中，搜索到3个老赖
            # for i in range(1,3):
            try:
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '暴风体育（北京）有限责任公司'")
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '北京暴风魔镜科技有限公司'")
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '暴风体育（北京）有限责任公司'")
                check = 1
            except:
                check = 0
            assert check==1
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()

        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：公司的老赖标签")
    def test_SerchDishonest_014(self):
        log.info(self.test_SerchDishonest_014.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("暴风北京")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信企业*'").click()
            # 校验
            elms = self.operation.new_elements(MobileBy.IOS_PREDICATE, "name == '老赖'")
            for i in range(0,2):
                try:
                    elms[i].get_attribute("name")
                    check=1
                except:
                    check=0
                assert check==1
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：内外名称相同")
    def test_SerchDishonest_015(self):
        log.info(self.test_SerchDishonest_015.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("司马朝")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '司马朝'").click()
            # 校验
            self.operation.new_elements(MobileBy.IOS_PREDICATE, "name == '司马朝'")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：1310821950身份证号是否包含在查询结果中")
    def test_SerchDishonest_016(self):
        log.info(self.test_SerchDishonest_016.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("1310821950")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验
            self.operation.new_elements(MobileBy.IOS_PREDICATE, "name LIKE '*1310821950*'")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：模糊查询*130984*；失信自然人 999+；校验下面的数字确实大于999")
    def test_SerchDishonest_017(self):
        log.info(self.test_SerchDishonest_017.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("130984")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：模糊查询*130984*；失信自然人 999+；校验下面的数字确实大于999
            self.operation.new_elements(MobileBy.IOS_PREDICATE, "name LIKE '*130984*'")
            self.operation.new_elements(MobileBy.IOS_PREDICATE, "name == '失信自然人 999+'")
            name = self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '搜索到 * 个老赖'").get_attribute("name")
            n = int(str(name).split(" ")[1])
            assert n>999
            print(str(name))
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：组织机构代码：798532048'")
    def test_SerchDishonest_018(self):
        log.info(self.test_SerchDishonest_018.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("798532048")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：组织机构代码：798532048
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信自然人*'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信企业*'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '组织机构代码：798532048'")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：组织机构代码：798532048'")
    def test_SerchDishonest_019(self):
        log.info(self.test_SerchDishonest_019.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("<>")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：校验失信自然人和失信企业为空
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信自然人 0'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name LIKE '失信企业 0'").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：组织机构代码：798532048'")
    def test_SerchDishonest_020(self):
        log.info(self.test_SerchDishonest_020.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：查老赖中间页
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '被列入“老赖”有什么影响 ？'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '什么是“老赖”？'").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：清除文本'")
    def test_SerchDishonest_021(self):
        log.info(self.test_SerchDishonest_021.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("11111")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：清除文本
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：不输入，无清除文本'")
    def test_SerchDishonest_022(self):
        log.info(self.test_SerchDishonest_022.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").click()
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：清除文本
            try:
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
                check=0
            except:
                check=1
            assert check==1
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：清除文本,恢复默认文案'")
    def test_SerchDishonest_023(self):
        log.info(self.test_SerchDishonest_023.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").send_keys("11111")
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：默认文案恢复。
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'")
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

    @getimage
    # @unittest.skip("校验：提示气泡'")
    def test_SerchDishonest_024(self):
        log.info(self.test_SerchDishonest_024.__doc__)
        try:
            # 点击 「全部」
            class_chain_a = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            class_chain_b = 'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]'
            self.operation.repeatedly_element(MobileBy.IOS_CLASS_CHAIN, class_chain_b, class_chain_a).click()
            # 点击查老赖，2个字符
            self.operation.new_element(MobileBy.ACCESSIBILITY_ID, "查老赖").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '输入人名/公司名/身份证号码/组织机构代码'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "value == '输入人名/公司名/身份证号码/组织机构代码'").click()
            # self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '1310821950'").click()
            # 校验：默认文案恢复。
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'Search'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '你还没有输入关键词'")
            # 返回
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'App Back'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'nav back new'").click()
        except Exception as e:
            log.error(error_format(e))
            raise e

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
# @Time    : 2020-04-29 09:30
# @Author  : wlx
# @File    : test_human_detail.py
import random
import unittest

from appium.webdriver.common.mobileby import MobileBy

from providers.common.base_client import BaseClick
from providers.common.base_operation import *

from providers.common.read_data import ReadExcel


class Test_Human_Detail(BaseClick):
    """人详情"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 获取excel
        cls.excel = ReadExcel().read_excel("human_detail")
        cls.user = cls.account.get_account()
        cls.vip_user = cls.account.get_account("vip", "0")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.account.release_account(account=cls.user, account_type="account", account_special="0")
        cls.account.release_account(account=cls.vip_user, account_type="vip", account_special="0")

    def search_input(self, search_type=1, value=None):
        """
        查老板搜索中间页搜索框搜索
        :param value: 搜索词
        :param search_type: 搜索类型 0:查公司 ，1:查老板
        """
        if search_type == 0:
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch company n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_input']).click()
            # search_text = self.operation.new_element(MobileBy.IOS_PREDICATE, "value CONTAINS '输入公司名称'")
            # search_text.send_keys(value)
            self.operation.send(MobileBy.IOS_PREDICATE, "value CONTAINS '输入公司名称'", value)
            self.log.info("输入关键字 {} 搜索".format(value))
            return value
        elif search_type == 1:
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch boss n'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_input']).click()
            # search_text = self.operation.new_element(MobileBy.IOS_PREDICATE, "value CONTAINS '输入老板信息'")
            # search_text.send_keys(value)
            self.operation.send(MobileBy.IOS_PREDICATE, "value CONTAINS '输入老板信息'", value)
            self.log.info("输入关键字 {} 搜索".format(value))
            return value

    def get_count(self, elment, index=1):
        str1 = elment.text
        self.log.info("打印数组--------", str1, "----------")
        a = str1.split()[index]
        a = str(a).replace("条", "")
        a = str(a).replace("人", "")
        a = str(a).replace("个", "")
        print(int(a))
        return int(a)

    def count_num(self, element):
        import re

        try:
            count_text = element.text
            print(count_text)
            match = re.search(r"([0-9]\d*)", count_text).group()
        except Exception as e:
            match = 0
        return int(match)

    @getimage
    def test_001(self):
        """未登录进入热搜人员详情页"""
        self.log.info(self.test_001.__doc__)
        try:
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'homeSearch  n'").click()
            hot_huamn = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['hot_human'])
            name = hot_huamn.text
            hot_huamn.click()
            detail_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_detail_name']).text
            self.assertEqual(name, detail_name, '首页热搜人员{}点击跳转到了{}人员详情页'.format(name, detail_name))

            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '自身风险:'").click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '密码登录'"),
                            '未登录用户人员详情页点击天眼风险未调起登录')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_trends']).click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '密码登录'"),
                            '未登录用户人员详情页点击人员动态未调起登录')
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_002(self):
        self.log.info(self.test_002.__doc__)
        try:

            self.search_input(value='马云')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()
            self.preprocessing.login(phone_num=self.user, password=self.account.get_pwd())

            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_vip_tip']),
                            '非VIP进入人员详情页无VIP限制')

            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '自身风险:'").click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_vip_tip']),
                            '非VIP用户人员详情页点击天眼风险无VIP限制')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['stock_right_map']).click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_vip_tip']),
                            '非VIP用户人员详情页点击股权穿透图无VIP限制')
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'ic pop off'").click()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_trends']).click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_vip_tip']),
                            '非VIP用户人员详情页点击人员动态无VIP限制')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_report_icon']).click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['report_download_icon']).click()
            self.assertTrue(self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_vip_tip']),
                            '非VIP用户人员详情页点击下载人员报告无VIP限制')
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == 'ic pop off'").click()
            self.preprocessing.logout()
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_003(self):
        self.log.info(self.test_003.__doc__)
        try:
            self.preprocessing.login(self.vip_user, self.account.get_pwd())
            self.search_input(value='马云')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()

            if self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '已监控'"):
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '已监控'").click()
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '确认'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '监控'").click()
            self.assertTrue(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '已监控'"), '人员详情页监控失败')

            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '自身风险:'").click()
            self.assertFalse(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '监控'"),
                             '人员详情页监控后，监控状态未同步到天眼风险页面')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_trends']).click()
            self.assertFalse(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '监控'"),
                             '人员详情页监控后，监控状态未同步到人员动态页面')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '已监控'").click()
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '确认'").click()
            self.assertTrue(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '监控'"), '人员详情页取消监控失败')

            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '自身风险:'").click()
            self.assertTrue(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '监控'"),
                            '人员详情页取消监控后，监控状态未同步到天眼风险页面')
            self.preprocessing.backtrack()

            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_trends']).click()
            self.assertTrue(self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '监控'"),
                            '人员详情页取消监控后，监控状态未同步到人员动态页面')
            self.preprocessing.backtrack()

        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_004(self):
        self.log.info(self.test_004.__doc__)
        try:
            self.search_input(value='马云')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()
            detail_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_detail_name']).text
            self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['human_report_icon']).click()
            report_select = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['report_type'].format(2))
            report_type = report_select.text
            report_select.click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['report_email']).click()
            if self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'"):
                self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '清除文本'").click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['report_email']).send_keys(
                'wanglixuan@tianyancha.com')
            self.operation.new_element(MobileBy.IOS_PREDICATE, self.excel['report_download_icon_vip']).click()

            report_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['order_field'].format(9)).text
            order_report_type = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,
                                                           self.excel['order_field'].format(10)).text
            email = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['order_field'].format(11)).text
            self.assertEqual(detail_name, report_name, '人员报告订单页显示名字{}与人员详情页名字{}不符'.format(report_name, detail_name))
            self.assertEqual(report_type, order_report_type,
                             '下载报告时选择的报告类型{}与订单页显示的报告类型{}不符'.format(report_type, order_report_type))
            self.assertEqual(email, 'wanglixuan@tianyancha.com', '订单页显示的email是{}'.format(email))

        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    @getimage
    def test_005(self):
        self.log.info(self.test_005.__doc__)
        try:
            self.search_input(value='王伟')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()
            # 获取人员详情页天眼风险count数
            risk_count = []
            for i in range(1, 4):
                count = self.count_num(
                    self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['risk_count'].format(i)))
                risk_count.append(count)
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '自身风险:'").click()
            #  获取天眼风险详情页实际count数
            e = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['item'])
            real_count = []
            for i in e:
                b = self.count_num(i)
                real_count.append(b)
            self.assertEqual(sum(risk_count), sum(real_count),
                             '人员详情页--天眼风险显示的count数{}与实际总count数{}不符'.format(sum(risk_count), sum(real_count)))
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    def test_006(self):
        self.log.info(self.test_006.__doc__)
        try:
            self.search_input(value='马云')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()

            legal = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['tab'].format(1))
            legal_count = self.count_num(legal)
            legal.click()
            real_count = self.count_num(self.operation.new_element(MobileBy.IOS_PREDICATE, "name CONTAINS '担任法定代表人'"))
            self.assertEqual(legal_count, real_count, '人员详情页法定代表人count检验错误')

            holder = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['tab'].format(2))
            holder_count = self.count_num(holder)
            holder.click()
            real_count = self.count_num(self.operation.new_element(MobileBy.IOS_PREDICATE, "name CONTAINS '担任股东的企业'"))
            self.assertEqual(holder_count, real_count, '人员详情页股东count检验错误')

            management = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['tab'].format(3))
            management_count = self.count_num(management)
            management.click()
            real_count = self.count_num(self.operation.new_element(MobileBy.IOS_PREDICATE, "name CONTAINS '担任高管的企业'"))
            self.assertEqual(management_count, real_count, '人员详情页担任高管count检验错误')

            control = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['tab'].format(4))
            control_count = self.count_num(control)
            control.click()
            real_count = self.count_num(
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['control_count']))
            self.assertEqual(control_count, real_count, '人员详情页实际控制权count检验错误')

            partner = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['tab'].format(5))
            partner_count = self.count_num(partner)
            partner.click()
            real_count = self.count_num(
                self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['partner_count']))
            self.assertEqual(partner_count, real_count, '人员详情页合作伙伴count检验错误')

            all_count = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['allcount'])) - 5
            add_count = legal_count + holder_count + management_count + control_count + partner_count
            self.assertEqual(all_count, add_count, '人员详情页实际公司item数{}和tab显示count之和{}不同'.format(all_count, add_count))
        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception
    @getimage
    def test_007(self):
        self.log.info(self.test_007.__doc__)
        try:
            self.search_input(value='王伟')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_trends']).click()
            count = self.count_num(self.operation.new_element(MobileBy.IOS_PREDICATE, "name CONTAINS '条动态'"))
            real_count = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['trend_count']))-1
            self.assertEqual(count,real_count, '人员详情页人员动态count数{}与实际条数{}不符'.format(count,real_count))

        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    def test_008(self):
        self.log.info(self.test_008.__doc__)
        try:
            self.preprocessing.login(self.vip_user, self.account.get_pwd())
            self.search_input(value='马云')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result_partner']).click()
            his = self.operation.new_element(MobileBy.IOS_PREDICATE, "name CONTAINS '曾经任职'")
            his_count = self.count_num(his)
            his.click()
            all_count = len(self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['his_company_item']))
            print(all_count)
            self.assertEqual(his_count, all_count, '人员详情页曾经任职count数{}与实际count数{}不符'.format(his_count, all_count))


        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception

    def test_009(self):
        self.log.info(self.test_009.__doc__)
        try:
            self.preprocessing.login(self.vip_user, self.account.get_pwd())
            self.search_input(value='李相赫')
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['search_boss_result']).click()
            detail_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['human_detail_name']).text
            self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '纠错'").click()
            error_name =self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.excel['error_name']).text
            self.assertEqual(detail_name, error_name, '人员详情页{}进入的纠错页面显示人名{}不对'.format(detail_name, error_name))

            error = self.operation.new_elements(MobileBy.IOS_CLASS_CHAIN, self.excel['error_type'])
            for i in error:
                error_type = i.text
                print(error_type)
                self.assertIn(error_type, self.excel['dimension_content'], '人员纠错页面维度选项{}没有'.format(error_type))


        except AssertionError:
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise Exception
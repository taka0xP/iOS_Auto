#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17
# @Author  : Soner
# @version : 1.0.0

import unittest
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import error_format
from providers.common.base_operation import getimage
from providers.common.base_client import BaseClick
from providers.all_services.operating import ServerOperating

from providers.common.read_data import ReadExcel


class TestAllServerCheckEntrance(BaseClick):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 获取excel
        cls.excel = ReadExcel().read_excel("all_server")
        cls.server_oper = ServerOperating(driver=cls.driver, excel=cls.excel, log=cls.log)\

    def setUp(self):
        # 点击 「全部」
        self.server_oper.click_all()


    @getimage
    def test_sy_jgq_p0_001(self):
        "首页金刚区-热门功能，全部只做入口校验"
        self.log.info(self.test_sy_jgq_p0_001.__doc__)
        try:
            # ========== 热门功能 ==========
            # 点击「天眼地图」
            # 校验 new 标签
            is_new = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.excel['ty_map_new'])
            self.assertTrue(is_new, "new标签不存在")
            self.server_oper.check_title(server_name="天眼地图", diff_con="天眼地图")
            self.preprocessing.backtrack()

            # 点击「查老赖」
            self.server_oper.check_title(server_name="查老赖", diff_con="查老赖")
            self.preprocessing.backtrack()

            # 点击「找电话」
            self.server_oper.check_text_field("找电话", "请输入企业名称")
            self.preprocessing.backtrack()

            # 附近公司
            self.server_oper.check_title(server_name="附近公司", diff_con="附近公司")
            self.preprocessing.backtrack()

            # 企业实名认证
            self.server_oper.check_title(server_name="企业实名认证", diff_con="选择认证套餐", tl=5)
            self.preprocessing.backtrack()

            # 身边老板
            self.server_oper.check_title(server_name="身边老板", diff_con="身边老板")
            self.preprocessing.backtrack()

            # 查商标
            self.server_oper.check_title(server_name="查商标", diff_con="查商标")
            self.preprocessing.backtrack()

            # 企业核名
            self.server_oper.check_title(server_name="企业核名", diff_con="企业名称检测")
            self.preprocessing.backtrack()

        except AssertionError as ae:
            raise self.failureException(ae)
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_p0_002(self):
        "首页金刚区-企业信息，全部只做入口校验"
        self.log.info(self.test_sy_jgq_p0_002.__doc__)
        try:
            # ========== 企业信息 ==========
            # 招聘
            self.server_oper.check_text_field(server_name="招聘", diff_con="请输入企业名称行业或职位")
            self.preprocessing.backtrack()

            # 招投标
            self.server_oper.check_text_field(server_name="招投标", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

            # 债券
            self.server_oper.check_text_field(server_name="债券", diff_con="请输入发行人、债券代码或名称")
            self.preprocessing.backtrack()

            # 查税号
            self.server_oper.check_text_field(server_name="查税号", diff_con="请输入企业名称或统一信用代码")
            self.preprocessing.backtrack()

            # 中国香港企业
            self.server_oper.check_text_field(server_name="中国香港企业", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

            # 中国台湾企业
            self.server_oper.check_text_field(server_name="中国台湾企业", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

            # 社会组织
            self.server_oper.check_text_field(server_name="社会组织", diff_con="请输入社会组织名称")
            self.preprocessing.backtrack()

            # 律师事务所
            self.server_oper.check_text_field(server_name="律师事务所", diff_con="请输入律师事务所名称")
            self.preprocessing.backtrack()

        except AssertionError as ae:
            self.log.error(error_format(ae))
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_p0_003(self):
        "首页金刚区-风险信息，全部只做入口校验"
        self.log.info(self.test_sy_jgq_p0_003.__doc__)
        try:
            # ========== 风险信息 ==========
            # 滑动一屏，确保下面的维度可点击
            self.operation.mobile_swipe(direction='up')

            # 诉讼
            self.server_oper.check_text_field(server_name="诉讼", diff_con="请输入诉讼号或企业名称")
            self.preprocessing.backtrack()

            # 法院公告
            self.server_oper.check_text_field(server_name="法院公告", diff_con="请输入企业名称、上诉方或被诉方")
            self.preprocessing.backtrack()

            # 税务评级
            self.server_oper.check_text_field(server_name="税务评级", diff_con="输入企业名称")
            self.preprocessing.backtrack()

            # 进出口信用
            self.server_oper.check_text_field(server_name="进出口信用", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

            # 司法拍卖
            self.server_oper.check_text_field(server_name="司法拍卖", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

            # 开庭公告
            self.server_oper.check_text_field(server_name="开庭公告", diff_con="请输入企业名称")
            self.preprocessing.backtrack()

        except AssertionError as ae:
            self.log.error(error_format(ae))
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise e

    @getimage
    def test_sy_jgq_p0_004(self):
        "首页金刚区-风险信息，全部只做入口校验"
        self.log.info(self.test_sy_jgq_p0_004.__doc__)
        try:
            # ========== 知识产权 ==========
            # 滑动一屏，确保下面的维度可点击
            self.operation.mobile_swipe(direction='up')

            # 查商标
            self.server_oper.check_title(server_name="查商标", diff_con="查商标")
            self.preprocessing.backtrack()

            # 专利
            self.server_oper.check_text_field(server_name="专利", diff_con="请输入专利名、专利号或企业名称")
            self.preprocessing.backtrack()

            # 著作权
            self.server_oper.check_text_field(server_name="著作权", diff_con="请输入著作权名、登记号或企业名")
            self.preprocessing.backtrack()

            # 网址
            self.server_oper.check_text_field(server_name="网址", diff_con="请输入公司名称或网址名称")
            self.preprocessing.backtrack()

        except AssertionError as ae:
            self.log.error(error_format(ae))
            raise self.failureException()
        except Exception as e:
            self.log.error(error_format(e))
            raise e









if __name__ == '__main__':
    unittest.main()

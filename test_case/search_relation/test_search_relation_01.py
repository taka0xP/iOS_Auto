# -*- coding: utf-8 -*-
# @Time    : 2020-04-21 14:02
# @Author  : XU
# @File    : test_search_relation_01.py
# @Software: PyCharm
import time
import unittest
from appium.webdriver.common.mobileby import MobileBy
from providers.common.logger import Logger, error_format
from providers.common.base_client import BaseClick
from providers.relation.operating import RelationOperate
from providers.relation.process import RelationProcess

log = Logger("查关系01").getlog()


class TestSearchRelation01(BaseClick):

    def setUp(self):
        self.relation_operate = RelationOperate(self.driver)
        self.elements = self.relation_operate.get_element()
        self.relation_process = RelationProcess(self.driver)

    def test_001_cgx_ss_p0(self):
        """点击热搜关系"""
        log.info(self.test_001_cgx_ss_p0.__doc__)
        try:
            relation_point_tag = self.relation_operate.hot_relation()
            home_page_tag = self.relation_process.relation_demo()
            self.assertTrue(relation_point_tag, "查关系：样例关系节点，展示失败")
            self.assertTrue(home_page_tag, "查关系：点击右上角天眼查logo，返回首页失败")
        except Exception as e:
            log.error(error_format(e))
        finally:
            self.preprocessing.back_index()

    def test_002_cgx_ss_p0(self):
        """输入查关系节点"""
        log.info(self.test_002_cgx_ss_p0.__doc__)
        vip_num = None
        try:
            vip_num = self.account.get_account(account_type='vip')
            vip_passwd = self.account.get_pwd()
            self.preprocessing.login(
                vip_num, vip_passwd)
            self.relation_process.relation_search()
        except Exception as e:
            log.error(error_format(e))
        finally:
            self.preprocessing.back_index()
            self.account.release_account(vip_num, account_type='vip')

    def test_003_cgx_ss_p0(self):
        """查关系-更多操作"""
        log.info(self.test_003_cgx_ss_p0.__doc__)
        try:
            self.relation_operate.hot_relation()
            share_tag = self.relation_process.relation_share()
            save_tag = self.relation_process.relation_save()
            time.sleep(3)
            scan_tag = self.relation_process.relation_scan()
            edit_tag = self.relation_process.relation_edit()
            self.assertTrue(share_tag, "查关系：更多操作，「分享」失败")
            self.assertTrue(save_tag, "查关系：更多操作，「保存」失败")
            self.assertTrue(scan_tag, "查关系：更多操作，「扫一扫」失败")
            self.assertFalse(edit_tag, "查关系：更多操作，「删减」失败")
        except Exception as e:
            log.error(error_format(e))
        finally:
            self.preprocessing.back_index()


if __name__ == '__main__':
    unittest.main()

import re
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from providers.common.base_client import BaseClick
from providers.common.base_operation import Operation, getimage
from providers.common.read_data import ReadExcel
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import warnings
import unittest
from providers.common.logger import Logger,error_format
import time

log=Logger("查公司02").getlog()


class TestSearchCompany1(BaseClick):

    a = ReadExcel()
    ELEMENT = a.read_excel("Search_company")

    def searh_keyword(self,keyword):
        '''搜索中间页搜索关键词'''
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys(keyword)
    def send_keyword(self,keyword):
        '''搜索中间页搜索关键词（有搜索记录）'''
        self.operation.send(MobileBy.IOS_PREDICATE,self.ELEMENT['middle_search_box'],keyword)
    def go_back(self):
        """返回上一页"""
        self.operation.mobile_drag_to_duration(0.2,0.5,0.6,0.5)
    def go_search_result(self,keyword,way):
        '''进入关键词搜索结果第一家公司'''
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys(keyword)
        time.sleep(2)
        if way == 1:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first1']).click()
        elif way == 2:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first2']).click()
        elif way == 3:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first3']).click()
        elif way == 4:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first4']).click()
        elif way == 5:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first5']).click()
        elif way == 6:
            self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first6']).click()
    def go_search_boss_result(self,keyword):
        '''进入关键词搜索结果第一家老板'''
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys(keyword)
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['search_boss_01']).click()
    def search_clear(self):
        '''输入框清除'''
        self.operation.new_element(MobileBy.IOS_PREDICATE,self.ELEMENT['search_clear']).click()
    def page_back(self):
        '''页面返回按钮'''
        self.operation.new_element(MobileBy.IOS_PREDICATE,self.ELEMENT['page_back']).click()

    # @getimage
    # def test_search_company_01(self):
    #     '''搜索中间页-身边老板'''
    #     self.log.info(self.test_search_company_01.__doc__)
    #
    #     goal_01 = '点击通讯录立即查看能进入「身边老板」页面'
    #     self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['company_search_box']).click()
    #     self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['view_now']).click()
    #     check_01 = self.operation.is_element(MobileBy.IOS_PREDICATE,"name == '开启通讯录权限'")
    #     log.info(check_01)
    #     if check_01 == True:
    #         self.operation.new_element(MobileBy.IOS_PREDICATE, "name=='立即开启'").click()
    #         self.operation.new_element(MobileBy.ACCESSIBILITY_ID,"OK").click()
    #         result_01 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID,'身边老板')
    #         self.assertTrue(result_01,msg='错误-%s'%goal_01)
    #     else:
    #         result_01 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID,'身边老板')
    #         self.assertTrue(result_01, msg='错误-%s' % goal_01)
    #
    #     self.go_back()

    def test_search_company_02(self):
        '''搜索中间页-热门搜索&最近搜索&最近浏览交互'''
        self.log.info(self.test_search_company_02.__doc__)

        goal_01 = '点击热门搜索模块能进入对应公司详情页'
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['company_search_box']).click()
        text_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['hot_search_01']).text
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['hot_search_01']).click()
        campany_name = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['company_name']).text
        self.assertIn(text_01,campany_name,msg='错误-%s' % goal_01)
        self.page_back()

        goal_02 = '点击最近搜索的记录进入搜索结果页'
        keyword = '腾讯科技'
        self.send_keyword(keyword)
        self.search_clear()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_search_01']).click()
        text_02 = self.operation.new_element(MobileBy.IOS_PREDICATE,self.ELEMENT['middle_search_box']).text
        self.assertEqual(keyword,text_02,msg='错误-%s' % goal_02)
        self.search_clear()

        goal_03 = '有最近搜索记录不展示热门搜索'
        result_03 = self.operation.is_element(MobileBy.IOS_PREDICATE,"name == '热门搜索'")
        self.assertFalse(result_03,msg='错误-%s' % goal_03)

        goal_04 = "有最近浏览记录不展示热门搜索"
        self.page_back()
        self.search_clear()
        result_04 = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '热门搜索'")
        self.assertFalse(result_04, msg='错误-%s' % goal_04)

        goal_05 = "点击最近搜索的一键清除icon弹出确认弹框"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['clear_01']).click()
        result_05 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID,'是否清空全部搜索记录？')
        self.assertTrue(result_05,msg='错误-%s' % goal_05)

        goal_06 = "最近搜索-确认弹框中选择取消能返回搜索中间页"
        self.operation.new_element(MobileBy.IOS_PREDICATE,"name == '取消'").click()
        result_06 = self.operation.is_element(MobileBy.IOS_PREDICATE,"name == '发现手机通讯录里的大老板，'")
        self.assertTrue(result_06,msg='错误-%s' % goal_06)

        goal_07 = "最近搜索-确认弹框中选择确认能清空最近搜索记录"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['clear_01']).click()
        self.operation.new_element(MobileBy.IOS_PREDICATE,"name == '确定'").click()
        result_07 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID,"最近搜索")
        self.assertFalse(result_07,msg='错误-%s' % goal_07)

        goal_08 = "点击最近浏览的一键清除icon弹出确认弹框"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['clear_01']).click()
        result_08 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, '是否清空全部浏览记录？')
        self.assertTrue(result_08, msg='错误-%s' % goal_08)

        goal_09 = "最近浏览-确认弹框中选择取消能返回搜索中间页"
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '取消'").click()
        result_09 = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '发现手机通讯录里的大老板，'")
        self.assertTrue(result_09, msg='错误-%s' % goal_09)

        goal_10 = "最近浏览-确认弹框中选择确认能清空最近浏览记录"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['clear_01']).click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, "name == '确定'").click()
        result_10 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, "最近浏览")
        self.assertFalse(result_10, msg='错误-%s' % goal_10)

        goal_11 = "删除最近搜索&最近浏览能展示热门搜索"
        result_11 = self.operation.is_element(MobileBy.IOS_PREDICATE, "name == '热门搜索'")
        self.assertTrue(result_11, msg='错误-%s' % goal_11)

        self.go_back()

    def test_search_company_03(self):
        '''搜索中间页-最近搜索展示规则'''
        self.log.info(self.test_search_company_03.__doc__)

        goal_01 = "搜索11条关键词查看最近搜索记录(倒序展示，最多展示10条)"
        search_list = ["百度1","百度2","百度3","百度4","百度5","百度6","百度7","百度8","百度9","百度10","百度11"]
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT["company_search_box"]).click()
        i = 0
        for i in range(len(search_list)):
            self.send_keyword(search_list[i])
            self.search_clear()
            i += 1
        text_01_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_search_01']).text
        text_01_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_search_10']).text
        log.info(text_01_01)
        log.info(text_01_02)
        if text_01_01 == search_list[10] and text_01_02 == search_list[1]:
            result_01 = True
        else:
            result_01 = False
        self.assertTrue(result_01,msg='错误-%s' % goal_01)

        goal_02 = "再次搜索相同关键词时查看最近搜索记录"
        self.send_keyword(search_list[10])
        self.search_clear()
        text_02_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_search_01']).text
        text_02_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_search_02']).text
        if text_02_01 == search_list[10] and text_02_02 == search_list[9]:
            result_02 = True
        else:
            result_02 = False
        self.assertTrue(result_02,msg='错误-%s' % goal_02)
        self.go_back()

    def test_search_company_04(self):
        '''搜索中间页-最近浏览展示规则'''
        self.log.info(self.test_search_company_04.__doc__)

        goal_01 = ["最近浏览-公司logo", "最近浏览-公司名称", "最近浏览-浏览标签","最近浏览-删除"]
        self.go_search_result('北京金堤科技有限公司',5)
        self.page_back()
        self.search_clear()
        result_01_01 = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_browse_logo'])
        self.assertTrue(result_01_01,msg='错误——%s'%goal_01[0])
        name_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_browse_name']).text
        self.assertEqual('北京金堤科技有限公司',name_text,msg='错误——%s'%goal_01[1])
        tag_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_browse_tag']).text
        self.assertEqual('今天浏览过',tag_text,msg='错误——%s'%goal_01[2])
        self.operation.is_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['recently_browse_del']).click()
        result_01_02 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID,'最近浏览')
        self.assertTrue(result_01_02,msg='错误——%s'%goal_01[3])

        goal_02 = ["最近浏览-老板logo", "最近浏览-老板名称", "最近浏览-浏览标签","最近浏览-删除"]
        self.go_search_boss_result('李彦宏')
        self.page_back()
        self.search_clear()
        result_02_01 = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_browse_logo'])
        self.assertTrue(result_02_01, msg='错误——%s' % goal_02[0])
        name_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_browse_name']).text
        self.assertEqual('李彦宏', name_text, msg='错误——%s' % goal_02[1])
        tag_text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_browse_tag']).text
        self.assertEqual('今天浏览过', tag_text, msg='错误——%s' % goal_02[2])
        self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['recently_browse_del']).click()
        result_02_02 = self.operation.is_element(MobileBy.ACCESSIBILITY_ID, '最近浏览')
        self.assertTrue(result_02_02, msg='错误——%s' % goal_02[3])











if __name__ == '__main__':
    unittest.main()
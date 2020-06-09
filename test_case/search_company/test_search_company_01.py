import re
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from providers.common.base_client import BaseClick
from providers.common.base_operation import Operation
from providers.common.read_data import ReadExcel
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import warnings
import unittest
from providers.common.logger import Logger,error_format
import time

log=Logger("查公司01").getlog()


class TestSearchCompany1(BaseClick):

    a = ReadExcel()
    ELEMENT = a.read_excel("Search_company")

    def searh_keyword(self,keyword):
        '''首页进入搜索中间页搜索关键词'''
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).click()
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys(keyword)

    def go_back(self):
        """返回上一页"""
        self.operation.mobile_drag_to_duration(0.2,0.5,0.6,0.5)

    def get_search_result(self,keyword,way):
        '''获取关键词搜索结果第一家公司名称'''
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys(keyword)
        time.sleep(2)
        if way == 1:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first1']).text
            return text
        elif way == 2:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first2']).text
            return text
        elif way == 3:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first3']).text
            return text
        elif way == 4:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first4']).text
            return text
        elif way == 5:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first5']).text
            return text
        elif way == 6:
            text = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['search_result_first6']).text
            return text


    def search_clear(self):
        '''输入框清除'''
        self.operation.new_element(MobileBy.IOS_PREDICATE,self.ELEMENT['search_clear']).click()

    def test_search_company_01(self):
        '''查公司-首页'''
        self.log.info(self.test_search_company_01.__doc__)

        goal_01 = '首页-输入框文案'
        text_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).text
        log.info(text_01)
        self.assertIn('输入公司名称、老板姓名、品牌名称等',text_01,msg='错误-%s'%goal_01)

        goal_02 = '首页-点击搜索框能跳转到搜索中间页'
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).click()
        result_01 = self.operation.is_element(MobileBy.IOS_PREDICATE,"name == '发现手机通讯录里的大老板，'")
        self.assertTrue(result_01,msg='错误-%s'%goal_02)
        self.go_back()


    def test_search_company_02(self):
        '''查公司-搜索中间页'''
        self.log.info(self.test_search_company_02.__doc__)

        goal_01 = '搜索中间页-输入框文案'
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).click()
        text_01 = self.operation.new_element(MobileBy.IOS_PREDICATE,self.ELEMENT['middle_search_box']).text
        self.assertEqual(text_01,'输入公司名称、老板姓名、品牌名称等',msg='错误-%s'%goal_01)
        self.go_back()

    def test_search_company_03(self):
        '''查公司-支持搜索范围'''
        self.log.info(self.test_search_company_03.__doc__)

        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).click()

        goal_01 = "输入公司全称能搜索到公司"
        result = self.get_search_result("北京金堤科技有限公司",5)
        self.assertEqual(result, "北京金堤科技有限公司", "错误————%s" % goal_01)
        self.search_clear()

        goal_02 = "输入统一信用代码能搜索到公司"
        result = self.get_search_result("9111010831813798XE",2)
        self.assertEqual(result, "北京金堤科技有限公司", "错误————%s" % goal_02)
        self.search_clear()

        goal_03 = "输入老板名称能搜索到公司"
        result = self.get_search_result("柳超",6)
        self.assertEqual(result, "北京金堤科技有限公司", "错误————%s" % goal_03)
        self.search_clear()

        goal_04 = "输入关键字能搜索到公司"
        result = self.get_search_result("百度",5)
        self.assertEqual(result, "北京百度网讯科技有限公司", "错误————%s" % goal_04)
        self.search_clear()

        goal_05 = "输入手机号能搜索到公司"
        result = self.get_search_result("18401651734",1)
        self.assertEqual(result, "贝壳找房（北京）科技有限公司", "错误————%s" % goal_05)
        self.search_clear()

        goal_06 = "输入座机号能搜索到公司"
        result = self.get_search_result("010-59328108",1)
        self.assertEqual(result, "北京链家旅居科技服务有限公司", "错误————%s" % goal_06)
        self.search_clear()

        goal_07 = "输入邮箱能搜索到公司"
        result = self.get_search_result("dufei@ke.com",1)
        self.assertEqual(result, "北京高策房地产经纪有限公司", "错误————%s" % goal_07)
        self.search_clear()

        goal_08 = "输入地址能搜索到公司"
        result = self.get_search_result("北京市海淀区西二旗西路2号院35号楼01层102-1",1)
        self.assertEqual(result, "贝壳找房（北京）科技有限公司", "错误————%s" % goal_08)
        self.search_clear()

        goal_09 = "输入曾用名能搜索到公司"
        result = self.get_search_result("链家网（北京）科技有限公司",1)
        self.assertEqual(result, "贝壳找房（北京）科技有限公司", "错误————%s" % goal_09)
        self.search_clear()

        goal_10 = "输入英文名能搜索到公司"
        result = self.get_search_result("Beijing Jindi Technology Co.,Ltd.",4)
        self.assertEqual(result, "北京金堤科技有限公司", "错误————%s" % goal_10)
        self.search_clear()

        goal_11 = "输入域名能搜索到公司"
        result = self.get_search_result("www.tianyancha.com",4)
        self.assertEqual(result, "北京天眼查科技有限公司", "错误————%s" % goal_11)
        self.search_clear()

        goal_12 = "输入经营范围能搜索到公司"
        result = self.get_search_result("二类6821医用电子仪器设备",1)
        self.assertEqual(result,"江苏中惠医疗科技股份有限公司", "错误————%s" % goal_12)
        self.search_clear()

        goal_13 = "输入商标名称能搜索到公司"
        result = self.get_search_result("企业秒懂",2)
        self.assertEqual(result,"北京金堤科技有限公司", "错误————%s" % goal_13)
        self.search_clear()

        goal_14 = "输入专利名称能搜索到公司"
        result = self.get_search_result("软基处理中塑料排水板的锚固装置",1)
        self.assertEqual(result,"中国二十冶集团有限公司", "错误————%s" % goal_14)
        self.search_clear()

        goal_15 = "输入股东/高管名称能搜索到公司"
        result = self.get_search_result("朱永贵",3)
        self.assertEqual(result, "中国二十冶集团有限公司", "错误————%s" % goal_15)
        self.search_clear()

        goal_16 = "输入项目名称能搜索到公司"
        result = self.get_search_result("蘑菇街",5)
        self.assertEqual(result, "杭州卷瓜网络有限公司", "错误————%s" % goal_16)
        self.search_clear()

        goal_17 = "输入股票代码能搜索到公司"
        result = self.get_search_result("601800",3)
        self.assertEqual(result, "中国交通建设股份有限公司", "错误————%s" % goal_17)
        self.search_clear()

        goal_18 = "输入拼音能搜索到公司"
        result = self.get_search_result("jiaotongjianshegufen",1)
        self.assertEqual(result, "中国交通建设股份有限公司", "错误————%s" % goal_18)
        self.search_clear()
        self.go_back()

    def test_search_company_04(self):
        '''搜索中间页-输入框+排序'''
        self.log.info(self.test_search_company_03.__doc__)

        goal_01 = '不输入字符时不展示一键清除按钮'
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box']).click()
        result_01 = self.operation.is_element(MobileBy.IOS_PREDICATE,self.ELEMENT['search_clear'])
        self.assertFalse(result_01,msg='错误-%s'%goal_01)

        goal_02 = "不输入字符时输入框右侧能正确展示为'取消'"
        text_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner1']).text
        self.assertEqual(text_02, '取消', msg='错误-%s' % goal_02)

        goal_03 = "输入一个字符后能正常展示一键清除按钮"
        self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).send_keys('a')
        result_03 = self.operation.is_element(MobileBy.IOS_PREDICATE,self.ELEMENT['search_clear'])
        self.assertTrue(result_03,msg='错误-%s'%goal_03)

        goal_04 = "输入一个字符时输入框右侧能正确展示为'取消'"
        text_04 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner1']).text
        self.assertEqual(text_04, '取消', msg='错误-%s' % goal_04)

        goal_05 = "输入关键字后点击一键清除能清空输入框内容"
        self.search_clear()
        text_05 = self.operation.new_element(MobileBy.IOS_PREDICATE, self.ELEMENT['middle_search_box']).text
        self.assertEqual(text_05, '输入公司名称、老板姓名、品牌名称等', msg='错误-%s' % goal_05)

        goal_06 = "点击取消能返回首页"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner1']).click()
        result_06 = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['company_search_box'])
        self.assertTrue(result_06,msg='错误-%s' % goal_06)

        goal_07 = ["输入两个字符时输入框右侧能正确展示为-排序", "输入两个字符时输入框左侧出现“返回”按钮"]
        self.searh_keyword('百度')
        text_07 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).text
        self.assertEqual(text_07,'排序',msg='错误-%s' % goal_07[0])
        result_07 = self.operation.is_element(MobileBy.IOS_PREDICATE,self.ELEMENT['page_back'])
        self.assertTrue(result_07,msg='错误-%s' % goal_07[1])

        goal_08 = "输入关键词点击排序时默认选项为'默认排序'"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).click()
        result_08 = self.operation.is_element(MobileBy.IOS_CLASS_CHAIN,self.ELEMENT['default_sort'])
        self.assertTrue(result_08, msg='错误-%s' % goal_08)

        goal_09 = "点击排序中-按注册资本从高到低"
        self.search_clear()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner1']).click()
        self.searh_keyword('北京金堤科技有限公司')
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).click()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['sort_02']).click()
        time.sleep(1)
        text_09_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['capital_01']).text
        text_09_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['capital_02']).text
        num_09_01 = re.sub("\D", "", text_09_01)
        num_09_02 = re.sub("\D", "", text_09_02)
        self.assertLess(num_09_02, num_09_01, "错误————%s" % goal_09)

        goal_10 = "点击排序中-按注册资本从低到高"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).click()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['sort_03']).click()
        time.sleep(1)
        text_10_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['capital_01']).text
        text_10_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['capital_02']).text
        log.info(text_10_01)
        log.info(text_10_02)
        num_10_01 = re.sub("\D", "", text_10_01)
        num_10_02 = re.sub("\D", "", text_10_02)
        self.assertLess(num_10_02, num_10_01, "错误————%s" % goal_10)

        goal_11 = "点击排序中-按成立日期从早到晚"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).click()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['sort_04']).click()
        time.sleep(1)
        text_11_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['date_01']).text
        text_11_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['date_02']).text
        num_11_01 = re.sub("\D", "", text_11_01)
        num_11_02 = re.sub("\D", "", text_11_02)
        self.assertLess(num_11_01, num_11_02, "错误————%s" % goal_11)

        goal_12 = "点击排序中-按成立日期从晚到早"
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['top_right_corner2']).click()
        self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['sort_05']).click()
        time.sleep(1)
        text_12_01 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['date_01']).text
        text_12_02 = self.operation.new_element(MobileBy.IOS_CLASS_CHAIN, self.ELEMENT['date_02']).text
        num_12_01 = re.sub("\D", "", text_12_01)
        num_12_02 = re.sub("\D", "", text_12_02)
        self.assertLess(num_12_02, num_12_01, "错误————%s" % goal_12)


if __name__ == '__main__':
    unittest.main()
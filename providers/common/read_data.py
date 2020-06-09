# -*- coding: utf-8 -*-
# @Time    : 2019-10-31 19:58
# @Author  : ZYF
# @File    : ReadData.py
import pymysql.cursors
import xlrd
import os


class ReadExcel():
    def read_excel(self, sheet_name):
        self.sheet_name = sheet_name
        # 找到文件
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 根目录
        # 打开Excel表格，填写路径
        workbook = xlrd.open_workbook(current_dir + '/data/' + '{}.xlsx'.format(sheet_name))

        # 打开sheet页
        sheet_value = workbook.sheet_by_name(self.sheet_name)

        # 获取sheet页行数
        row_nu = sheet_value.nrows

        # 取表格数据到字典
        a = []
        b = []
        for i in range(1, row_nu):
            self.row_value1 = sheet_value.row_values(i)[0]  # 取表格里面的值
            self.row_value2 = sheet_value.row_values(i)[1]  # 取表格里面的值
            a.append(self.row_value1)
            b.append(self.row_value2)
        excel_dict = dict(zip(a, b))
        return excel_dict


config = {
    'host': '10.2.22.232',
    'port': 3306,
    'user': 'root',
    'password': 'stdgn',
    'db': 'android_auto_elements',
    'charset': 'utf8'
}


class DB(object):
    def __init__(self):
        self.db = pymysql.connect(**config)
        self.cursor = self.db.cursor()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            print('sql语句执行失败')

    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()

    def get_element(self, table_name, ele_type):
        """
        :param ele_type: 需要获取元素模块类型，1-查公司，2-查老板， 3查关系， 4-查老赖，5-人员详情页，6-公司详情页，7-企业预核名'
        :param table_name: 数据库元素存放版本表（eg: elements_v11.8.0）
        :return: 字典类型：格式： {'元素名称': '元素'}
        """
        elements = {}
        sql = "SELECT ele_key, ele_value FROM `{}` WHERE `ele_mode`='{}';".format(table_name, ele_type)
        result = self.execute_sql(sql)
        self.close()
        for ele in result:
            elements[ele[0]] = ele[1]
        return elements


if __name__ == '__main__':
    a = ReadExcel()
    b = a.read_excel('Search_boss')
    print(b)
    # db = DB()
    # print(db.get_element('elements_v11.8.0', '5'))

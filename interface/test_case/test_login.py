#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie
import unittest,os
from ddt import ddt,data
from tools.http_request import HttpRequest
from tools.project_path import data_dir
from tools.read_excel import ReadExcel

data_file = os.path.join(data_dir,'test_data.xlsx')
test_data = ReadExcel(data_file,'login').get_data()

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self,case_data):
        res = HttpRequest.http_request(case_data['url'],eval(case_data['data']),case_data['method'])
        try:
            self.assertEqual(str(case_data['expected']),res.json()['code'])
            self.TestResult = 'PASS'
        except Exception as e:
            self.TestResult = 'Failed'
            print('接口返回的信息是：{0}'.format(e))
            raise e
        finally:
            ReadExcel(data_file,'login').write_back_data(case_data['case']+1,self.TestResult,str(res.json()))
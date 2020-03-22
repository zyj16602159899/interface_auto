from tools.http_request import HttpRequest
from tools.project_path import data_dir
from tools.read_excel import ReadExcel
from tools.get_cookie import GetCookie
import os

#方法一：cookie使用全局变量！
# COOKIE = None
# data_file = os.path.join(data_dir,'test_data.xlsx')
#
# def run(test_data):
#
#     global COOKIE
#     for item in test_data:
#         print('正在测试的用例是{0}'.format(item['title']))
#         res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],cookie=COOKIE)
#         if res.cookies:
#             COOKIE = res.cookies
#         print('请求的结果是{0}'.format(res.json()))
#         ReadExcel(data_file,'recharge').write_back_data(item['case']+1,str(res.json()))

#方法二：cookie使用反射！
data_file = os.path.join(data_dir,'test_data.xlsx')

def run(test_data):

    for item in test_data:
        print('正在测试的用例是{0}'.format(item['title']))
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],cookie=getattr(GetCookie,'COOKIE'))
        if res.cookies:
            setattr(GetCookie,'COOKIE',res.cookies)
        print('请求的结果是{0}'.format(res.json()))
        ReadExcel(data_file,'recharge').write_back_data(item['case']+1,str(res.json()))

test_data = ReadExcel(data_file,'recharge').get_data()
run(test_data)
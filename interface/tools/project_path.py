import os

project_dir = os.path.dirname(os.path.dirname(__file__))

#配置文件目录
conf_dir = os.path.join(project_dir,'conf')
#测试数据目录
data_dir = os.path.join(project_dir,'data')
#测试用例目录
case_dir = os.path.join(project_dir,'test_case')
#测试结果目录
result_dir = os.path.join(project_dir,'result')

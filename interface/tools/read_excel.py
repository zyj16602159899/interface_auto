from openpyxl import load_workbook
import os
from project_path import data_dir

data_file = os.path.join(data_dir,'test_data.xlsx')

class ReadExcel:

    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
    
    def open_file(self):
        self.workbook = load_workbook(self.file_name)
        self.sheet = self.workbook[self.sheet_name]
    
    def close_file(self):
        self.workbook.close()

    def get_data(self):
        self.open_file()
        test_data = []
        for i in range(2,self.sheet.max_row+1):
            row_data = {}
            row_data['case'] = self.sheet.cell(i,1).value
            row_data['url'] = self.sheet.cell(i,2).value
            row_data['data'] = self.sheet.cell(i,3).value
            row_data['title'] = self.sheet.cell(i,4).value
            row_data['method'] = self.sheet.cell(i,5).value
            test_data.append(row_data)
        return test_data


data = ReadExcel(data_file,'login').get_data()
for item in data:
    print(item)
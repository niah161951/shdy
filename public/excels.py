#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:01
import xlrd

class ExcelUtil():
    def __init__(self):

        # excelPath = r'C:\Users\Lenovo\Desktop\生产验证\生产验证结果.xlsx'
        excelPath = r'C:\Users\Lenovo\Desktop\test.xlsx'
        sheetName = "Sheet1"
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)

       # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        # else:
            # r = []
            # j = 1
        r = []
        for i in range(1, self.rowNum):
            s = {}
            # 从第二行取对应values值
            values = self.table.row_values(i)
            for x in range(self.colNum):
                s[self.keys[x]] = values[x]
            r.append(s)
        return r


def method_name():
    data = ExcelUtil()
    s = data.dict_data()
    for i in s:
        print(i.get('商户号'))


if __name__ == "__main__":
    method_name()

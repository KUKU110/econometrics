# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:07:13 2017

@author: Administrator
"""

# tutorial about python-excel

# opening workbooks
'''
workbooks can be loaded either from a file, an mmap.mmap object or from a string:
'''
import numpy as np
from mmap import mmap, ACCESS_READ
from xlrd import open_workbook
f=open_workbook('000300_price.xlsx')
print(f)

with open('000300_price.xlsx','rb') as f:
    print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
aString=open('000300_price.xlsx','rb').read()
print(open_workbook(file_contents=aString))
# 上面的代码没看懂，什么玩意儿？

# navigating a workbook
# here is a simple example of workbook navigation
from xlrd import open_workbook
wb=open_workbook('000300_price.xlsx')
for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        values=[]
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(','.join(values))
    print

'''
the xlrd.Book object return by open_workbook contains all information to do with
the workbook and can be used to retrieve individual sheets within the workbook.
the nsheets attribute is an integer containing the number of sheets in the workbook.
the attribute, incombination with the sheet_by_index method, is the most common way of 
retrieving individual sheets.
the sheet_names method returns a list of uncodes containing the name of all sheets
in the workbook. individual sheets can be retrieved using these names by way of the
sheet_by_name function.
the results of the sheets method can be interated over to retrieve each of the sheets in the workbook
'''

from xlrd import open_workbook
book=open_workbook('000300_price.xlsx')
print(book.nsheets)
for sheet_index in range(book.nsheets):
    print(book.sheet_by_index(sheet_index))
for sheet_name in book.sheet_names():
    print(book.sheet_by_name(sheet_name))
for sheet in book.sheets():
    print(sheet)
    
'''
the xlrd.sheet.Sheet objects returned by any of the methods described above contain
all the information to do with a worksheet and its contents
the name attribute ia s unicode representing the name of the worksheet
the nrows and ncols attributes contain the number of the rows and the number of columns,
in the worksheet
'''
book.sheet_by_index(1).name   # sheet 的编号也是从0开始的
from xlrd import open_workbook,cellname
book=open_workbook('000300_price.xlsx')
sheet=book.sheet_by_index(0)
print(sheet.name)
print(sheet.nrows)
print(sheet.ncols)  # 已经使用的行数和列数
data=np.zeros((sheet.nrows,sheet.ncols)) # 不知道怎么创建空的数组，还有就是这里为什么要用两个括号？
for row_index in range(sheet.nrows):
    for col_index in range(sheet.nrows):
        # print(cellname(row_index,col_index),'-')
        # print(sheet.cell(row_index,col_index).value)
        data[row_index,col_index]=(sheet.cell(row_index,col_index).value) # list 应该是只有一行的形式
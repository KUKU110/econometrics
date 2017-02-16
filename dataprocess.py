# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:04:31 2017

@author: Administrator
"""

# for the financial risk management 

# 1. load the data from excel files
from xlrd import open_workbook
import pandas as pd
import numpy as np

#data1=open_workbook('data1.xlsx')
#data2=open_workbook('data2.xlsx')
#data3=open_workbook('data3.xlsx')
#
#sheet11=data1.sheet_by_index(0)
#sheet12=data1.sheet_by_index(1)
#sheet13=data1.sheet_by_index(2)
#
## 读入三个表中的数据
## sheet11
#data=np.zeros((sheet11.nrows,sheet11.ncols))
#for row_index in range(sheet11.nrows):
#    for col_index in range(sheet11.ncols):
#        data[row_index,col_index]=(sheet11.cell(row_index,col_index).value) # list 应该是只有一行的形式
## can not convert string to float 

# 利用pandas可以直接读取其中的数据
xls_file1=pd.ExcelFile('data1.xlsx')
table11=xls_file1.parse('Sheet1')
# 先利用table11中的数据做一次

# table11的数据处理程序
# 为保留特定的行，首先对数据进行转置，然后再进行处理
# table11=table11.transpose() # 转置操作
# 将股票代码填入空列
# [cols,columns]=table11.shape  # 为啥shape后面不加括号就行，加了括号就报错
# shape 是dataframe的属性，不是方法
table11.insert(table11.shape[1],'code',np.nan*table11.shape[0])
for i in range(6,table11.shape[1],8):
    for j in range(2,147):       
        if j==2:
            table11.iloc[j,i]='code'
        else:
            table11.iloc[j,i]=table11.iloc[0,i-6]
table11=table11.drop([np.nan,'日期']) # 其中名称为nan的行无法删除，报错
# 改成np.nan就可以了，这里行的名称是真的没有，不是'nan'

# 怎么做才可以自己设定dataframe的index呢？
table11.insert(0,'Date',table11['Unnamed: 7'])

# 把数据的第一行设置为行名称
# 可以采用新方法，重新生成一个新的frame
table11=table11.rename(columns=table11.iloc[0])
table11=pd.DataFrame(data=table11.iloc[1:,:]) # 后面的必须是一个list才行
# 为什么数据都是nan？ 或许是因为导入的数据是DataFrame,需要列相匹配

column_number=8 # 一只股票的数据占有8列
row_number=table11.shape[0] # 获取dataframe的行数和列数采用这种方式来做

# use loop to reorganize the data
# 利用concat函数进行数据的块状整理
data=table11.iloc[:,:column_number]
for i in range(1,int(table11.shape[1]/column_number)):
    # range中的数必须是整数类型
    startcol=i*column_number
    endcol=startcol+column_number
    ans=table11.iloc[:,i*column_number:(i+1)*column_number]
    data=pd.concat([data,ans])
del([ans,table11])
data.to_csv('mydata.csv')
# convert the dataframe to a panel-like structure
# 或许不用转换为面板数据类型也能做研究

# 处理市场收益率数据
mrtdata=pd.ExcelFile('mrtdata.xlsx')
mrtprice=mrtdata.parse('指数价格')
# 计算从2002.1.4到2016.12.30的沪深300指数收益率数据



        
        



# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:45:33 2017

@author: Administrator
"""

# summaries
import numpy as np
import pandas as pd
# 创建对象，创建Series和DataFrame
# 创建Series
# 利用list创建Series
mydata=np.random.randn(10)
mydata1=np.random.randn(10,5)
myseries=pd.Series(data=mydata)
# myseries1=pd.Series(data=mydata1)  mydata1是二维的，不能用来创建Series
# data must be one dimensional, but how to transform an array to one dimensional?
# 传入Series的数据必须是一维的，
myframe=pd.DataFrame(data=mydata1,index=list(range(1,11)),columns=['a','b','c','d','e'])

# viewing data, slicing
# 截取整行
# 使用loc或者iloc从DataFrame中截取整行
# 单独一行，选取第一行
a=myframe.loc[1]
b=myframe.iloc[0,:]
c=myframe[0:2] # 选取多行
# 单独一列，选取第三列
a=myframe.iloc[:,2]
b=myframe['c']
# 选取连续的多行多列，使用iloc函数
a=myframe.iloc[1:3,2:4]
# 选取不连续的多行多列，同样使用iloc函数
b=myframe.iloc[[1,3],[2,4]]

# 选取满足条件的数据
a=myframe[myframe.iloc[:,2]>0]

# 设置DataFrame的数据
myframe.iloc[0,1]=10000































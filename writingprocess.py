# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:23:22 2017

@author: Administrator
"""

import sys
sys.path.append("D:\econometrics")
import numpy as np
import basicfunctions as bf
import xlrd
import os
os.chdir('D:\econometrics')
data=xlrd.open_workbook('000300_price.xlsx')
data1=data.sheet_by_index(1)
x=np.array([[1,2],[3,4]])
y=bf.p_x(x)
m=np.mat(x)
ans=m*(m.T*m).I*m.T
z=bf.m_x(x)
(row,column)=m.shape

ols=bf.OLS()
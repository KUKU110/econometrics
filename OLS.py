# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:02:29 2017

@author: Administrator
"""

class OLS(y,x): # x should include a constant regressor
    def __init__(self):
        self.y=np.mat(y)
        self.x=np.mat(x)
        self.beta=[]
    def regress(self):
        self.beta=(self.x.T*self.x).I*self.x.T*self.y
        
       
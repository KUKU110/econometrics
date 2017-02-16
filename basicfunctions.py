# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:58:34 2017

@author: Joey
"""

'''
this module provides basic function for calculation in econometrics
the module is developed based on the module numpy, all the arguments in a funciton must be an ndarray
'''
import numpy as np
from scipy import stats

##
def p_x(x):
    # use the function mat to transform an array to a matrix
    m=np.mat(x)
    return m*((m.T*m).I)*m.T
 
## 
def m_x(x):
    (row,column)=x.shape
    return np.eye(row)-p_x(x)

##
class OLS: # x should include a constant regressor
    def __init__(self,y,x):
        self.y=np.mat(y,)
        self.x=np.mat(x)
        (self.n,self.k)=self.x.shape()
        self.beta_hat=(self.x.T*self.x).I*self.x.T*self.y
        self.y_hat=self.x*self.beta
        self.residuals=self.y-self.y_hat
        self.TSS=self.y.var(0)
        self.ESS=self.y.var(0)
        self.SSR=self.residuals.var(0)
        self.s2=self.SSR/(self.n-self.k)
        self.cov_beta_hat=self.s2*(self.x.T*self.x).I
        self.R2=self.ESS/self.TSS
        self.R2_adjusted=1-(self.n-1)*self.y.T*m_x(self.x)*self.y/((self.n-self.k)*\
        self.y.T*m_x(np.ones(self.n,1))*self.y)
        self.var_beta_hat=np.diag(self.cov_beta_hat)
        self.t=[m/n for m in self.beta_hat for n in self.var_beta_hat] # a list
        self.p_t=(1-stats.norm.cdf(self.t))*2  # 2-tail test
        self.F=self.ESS/(self.k-1)/self.SSR*(self.n-self.k)

        


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:55:20 2017

@author: Administrator
"""

# pandas tutorial

# create data
# the initial set of baby names and birth rates
import pandas as pd
import numpy as np
names=['bob','jessica','mary','john','mel']
births=[34,48,49,38,23]
# to merge these 2 list together, we will use the zip function
babydataset=list(zip(names,births))
df=pd.DataFrame(data=babydataset,columns=['names','births'])
'''
export the dataframe to a csv file. the function to_csv will be used to export 
the file. the only parameters we will use is index and header. setting these parameters
to true will prevent the index and the header names from being exported
'''
df.to_csv('births1880.csv',index=False,header=False)

# get data
# to pull in the csv file, we will use the pandas function read_csv
Location = r'C:\Users\david\notebooks\births1880.csv'
df = pd.read_csv(Location)
'''
if we wanted to give the columns specific names, we would have to pass another
parameter called names
'''

# prepare data

# pandas cookbook
# if-then/if-then-else on one column, and assignment to another one or more columns
df=pd.DataFrame({'aaa':[4,5,6,7],'bbb':[10,20,30,40],'ccc':[100,50,-30,-50]})
# 根据一列的数值为条件设定另一列的数值
# an if-then on one column
df.ix[df.aaa>=5,'bbb']=-1  # 设定满足条件的列数值
df.ix[df.aaa>5,'ccc']=0
df.ix[df.aaa>5,['aaa','bbb']]=555 # 设置多列的数值
# or use pandas where after you've set up a mask, or if then else using numpy's where

# splitting
# split a frame with a boolean criterion
df=pd.DataFrame({'aaa':[4,5,6,7],'bbb':[10,20,30,40],'ccc':[100,50,-30,-50]})
dflow=df[df.aaa<5]
dfhigh=df[df.aaa>=5]

# building criteria
# select with multi-column criteria 
df=pd.DataFrame({'aaa':[4,5,6,7],'bbb':[10,20,30,40],'ccc':[100,50,-30,-50]})
newseries=df.loc[(df['bbb']<25)&(df['ccc']>-40),'aaa'] # 为什么返回的是一个series？
# with assignment modifies the dataframe

# dynamically reduce a list of criteria using a binary operators
crit1=df.aaa<5.5
crit2=df.bbb==10
crit3=df.ccc>-40
allcrit=crit1 & crit2 & crit3 # 得到的是一个一列是series
# or it could be done with a list of dynamically built criteria
critlist=[crit1,crit2,crit3]
allcrit=pd.functools.reduce(lambda x,y: x&y,critlist) # 这个是什么函数，帮助文件都查不到
df[allcrit]

# selection
# using both row labels and value conditions
df=pd.DataFrame({'aaa':[4,5,6,7],'bbb':[10,20,30,40],'ccc':[100,50,-30,-50]})
df[(df.aaa<6)&(df.index.isin([0,2,4]))]
# use loc for label-oriented slicing and iloc positional slicing
data={'aaa':[4,5,6,7],'bbb':[10,20,30,40],'ccc':[100,50,-30,-50]}
df=pd.DataFrame(data=data,index=['foo','bar','boo','kar'])
'''
there are 2 explicit slicing methods, with a 3rd general case:
1. positional-oriented(python slicing style: exclusive of end)
2. label-oriented(non-python slicing style: inclusive of end)
3. general
'''
df.loc['bar':'kar']
a=df.loc[['bar','boo']] # 如果选取多行，需要用两个方括号
df.ix[0:3] # same as .iloc[0:3]  # loc 是根据行label来选取，而iloc是根据数字位置来获取
df.ix['bar':'kar']
df.ix[['bar','kar']]

# panels
'''
extend a panel frame by transposing, adding a new dimension and transposing back
to the original dimensions
'''
rng=pd.date_range('1/1/2013',periods=100,freq='D')
data=np.random.randn(100,4)
cols=['a','b','c','d']
df1,df2,df3=pd.DataFrame(data,rng,cols),pd.DataFrame(data,rng,cols),pd.DataFrame(data,rng,cols)
pf=pd.Panel({'df1':df1,'df2':df2,'df3':df3})
# assignment using transpose
pf=pf.transpose(2,0,1)  # 代码没有打完，是在pandastutorial文件387页

# new columns
# efficiently and dynamically creating new columns using applymap
source_cols=df.columns
new_cols=[str(x)+'cat' for x in source_cols]
categories={1:'alpha',2:'beta',3:'charlie'}
df[new_cols]=df[source_cols].applymap(categories.get)

# multiindexing
# 将某一列的数设置为index，但是设置为index 的这列数在源数据中就没有了，
m=df.set_index(df['ccc'])  # 这个函数会返回一个新的dataframe对象
df=pd.DataFrame({'row':[0,1,2],'one_x':[1,1,1],'one_y':[1.2,1.2,1.2],\
'two_x':[1.1,1.1,1.1],'two_y':[1.22,1.22,1.22]})
# as labelled index
df=df.set_index(df['row'])
# with hierarchical columns
df.columns=pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])

# arithmetic
# performing arithmetic with a multi-index that needs broadcasting
cols=pd.MultiIndex.from_tuples([(x,y) for x in ('a','b','c') for y in ('o','i')])
df=pd.DataFrame(data=np.random.randn(2,6),index=['n','m'],columns=cols)


# 10 minutes to pandas
# object creation
s=pd.Series([1,2,5,np.nan,9])
# creating a dataframe by passing a numpy array, with a datetime index and labeled columns
dates=pd.date_range('20150101',periods=6) # create a datetime index
df=pd.DataFrame(data=np.random.randn(6,4),index=dates,columns=list('abcd'))
# creating a dataframe by passing a dict of objects that can be converted to series-like
df2=pd.DataFrame({'A':1,'B':pd.Timestamp('20150101'),'C':pd.Series(1,index=list(range(4))),'D':np.array([3]*4)})

# viewing data
df.head() # return first n rows of dataframe
df.tail() # return last n rows
# describe shows a quick statistic summary of your data
df.describe()
# transposing your data
df.T
# sorting by an axis
df.sort_index(axis=1,ascending=False)
# sorting by values
df.sort_values(by='b')

# selection
# we recommend the optimized pandas data access methods, at/iat/loc/iloc/ix
# getting
# selecting a single column, which yields a Series, equivalent to df.a
# 按列选择数据
df[['a','b']]
df.a
# selecting via[],which slices the rows
# 按行选择数据
df[0:3] # 按数字选择特定的几行
df['20130102':'20130104'] # 按照行名选择几行
# selection by label
# for getting a cross section using a label
# 选择行
df.loc[dates[0]]
# selecting on a multi-axis by label
# 选择多列,原来loc也可以选择列，只是需要一些变化
df.loc[:,['a','b']]
# showing label slicing, both endpoints are included
df.loc['20150102':'20150104',['a','b']]
df.loc['20150102':'20150104','a':'c']  # 选择多行多列
# selection by position
df.iloc[3]
# by integer slices, acting similar to numpy/python
df.iloc[3:5,0:2]  # 利用iloc进行行列切片
# by lists of integer position locations, similar to numpy/python style
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
# for slicing columns explicitly
df.iloc[:,1:3]
# for getting a value explicitly
df.iloc[1,1]
# for getting fast access to a scalar
df.iat[1,1]
# boolean indexing
# using a single column's values to select data
df[df.a>0]
# setting
# setting a new column automatically aligns the data by the indexes
s1=pd.Series(list(range(1,7)),index=pd.date_range('20130102',periods=6))
# 将range转换成list需使用list函数，直接用方括号将range括起来不行
df['f']=s1  # 将Series设为dataframe中的一列
# setting values by label
df.at[dates[0],'a']=0
# setting values by position
df.iat[0,1]=0
# setting by assigning with a numpy array
df.loc[:,'d']=np.array([5]*len(df)) # len 返回的是行数，怎么返回列数
# 将正数都设为负数
df2[df2>0]=-df2 # 将数值设置为负数
# missing data
'''
pandas primarily uses the value np.nan to represent missing data. it is by
default not included in computations.
'''
df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['e'])
df1=df1.loc[dates[0]:]
# to drop any rows that have the missing data
df1.dropna(how='any')
# filling missing data
df1.fillna(value=5)
# to get the boolean mask where values are nan
pd.isnull(df1)

# operations
# stats
df.mean() # 按列求均值
df.mean(1) # 按行求均值
# apply functions to the data
df.apply(np.cumsum) # return a new dataframe
a=df.apply(lambda x: x.max()-x.min())  # 按列应用函数
# merge
# concat
'''
pandas provides various facilities for easily combing together series, DataFrame,
and panel objects with various kinds of set logic for the indexes and relational
algebra functionality in the case of join/merge-type operations
'''
df=pd.DataFrame(np.random.randn(10,4))
pieces=[df[:3],df[3:7],df[7:]]
a=pd.concat(pieces)
# join
left=pd.DataFrame({'key':['foo','hello'],'lval':[1,2]})
right=pd.DataFrame({'key':['foo','hello'],'rval':[4,5]})
pd.merge(left,right,on='key')
# append
# append rows to a dataframe
df=pd.DataFrame(np.random.randn(8,4),columns=['a','b','c','d'])
s=df.iloc[3]
df.append(s,ignore_index=True)
# grouping
'''
by 'group by' we are referring to a process involving one or more of the following steps
splitting the data into groups based on some criteria
applying a function to each group independently
combining the results into a data structure
'''


















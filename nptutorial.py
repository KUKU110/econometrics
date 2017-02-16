# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:47:16 2017

@author: Administrator
"""

# numpy tutorial

# the basics
'''
numpy's main object is the homogeneous multidimensional array,
it is a table of elements, all of the same type, indexed by a tuple of positive integers
numpy's array class is called ndarray. numpy.array is not the same as the standard
python library class array.array, which only handles one-dimensional arrays and offers 
less functionality. attributes of an ndarray objects are:
ndarray.ndim, ndarray.shape, ndarray.size, ndarray.dtype, ndarray.itemsize, ndarray.data
we can access the elements in an array using indexing facilities
'''
import numpy as np
a=np.arange(15).reshape(3,5) # np.arange return evenly spaced values within a given interval
# arange([start,],stop[,step,], dtype=none)
a.shape

# array creation
'''
several ways to create arrays
1. create an array from a regular python list or tuple using the array function
'''
a=np.array([2,3,4]) # create an array using a list
# array transforms sequences of sequences into 2-dimensional arrays
b=np.array([(1,2,3),(4,5,6)])
# the type of the array can also be explicitly specified at creation time
c=np.array([[1,2],[3,4]], dtype=complex) # 纳入array的数据都需要用方括号括起来？
'''
often, the elements of an array are originally unknown, but its size is known.
hence, numpy offers several functions to create arrays with initial placeholder content.
the function zeros creates an array full of zeros, the function ones create an array full
of ones, and the function empty creates an array whose initial contents is random
and depends on the state of the memory.
'''
np.zeros((3,4))
np.ones((2,3,4),dtype=np.int16)
np.empty((2,3))

'''
to create a sequences of numbers, numpy provides a function analogous to range that
returns arrays instead of lists
'''
np.arange(10,30,5)  # array([10, 15, 20, 25])
np.arange( 0, 2, 0.3 )  # array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])

'''
when arange is used with floating point auguments, it is generally not possible
to predict the number of elements obtained. for this reason, it's usually better
to use the function linspace that receives as an augument the number of elements we want, 
instead of the step.
'''
from numpy import pi
np.linspace(0,2,9)  # 9numbers from 0 to 2
# array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
x=np.linspace(0,2*pi,100)

'''
to create sample numbers, we can also use the following functions
numpy.random.rand, numpy.random, fromfunction, fromfile
'''

# printing array
'''
when you print an array, numpy displays it in a similiar way to nested lists,
but with the following layout:
1. the last axis is printed from left to right
2. the second-to-last is printed from top to bottom
3. the nested are also printed from top to bottom, with each slice seperated from
the next by an empty line
'''

# basic operations
'''
arithmetic operators on arrays apply elementwise, a new array is created and filled
with the result
'''
a=np.array([20,30,40,50])
b=np.arange(4)  # array([0, 1, 2, 3])
c=a-b  # array([20, 29, 38, 47])
b**2  # array([0, 1, 4, 9])
a<35 # array([ True, True, False, False], dtype=bool)

'''
unlike in many matrix languages, the product operator * operates elementwise in 
numpy arrays. the matrix product can be performed using the dot function
'''
a=np.array([1,1],[0,1])
b=np.array([2,0],[3,4])
a*b # elementwise product
a.dot(b) # matrix product
np.dot(a,b) # another matrix product, the result is like the following

'''
some operations, such as += and *=, act in place to modify an existing array rather
than create a new one
'''
a=np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a*=3 #array([[3, 3, 3],[3, 3, 3]])
b+=a
a=a+b
'''
a+=b will result in an error
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64')
 with casting rule 'same_kind'
but a=a+b can do it, I don't know why
'''

'''
when operating with arrays of different types, the type of the resulting array
corresponds to the more general or precise one
'''

# indexing, slicing and iterating
a=np.arange(10)**3
a[2]
a[2:5]
a[:6:2]=1000 # equivalent to a[0:6:2]=1000, from start to position 6, set every 2nd element to 1000
# reverse a
a[::-1]

'''
multidimensional arrays can have one index per axis, these indices are given in a tuple seperate by commas
'''
b[2,3]
b[0:5, 1]  
b[ : ,1] 
b[1:3, : ]

# shape manipulating
# an array has a shape given by the number of elements along each axis
a = np.floor(10*np.random.random((3,4)))
[m,n]=a.shape
'''
the shape of an array can be changed with various commands. note that the following
3 commands all return a modified array, but do not change the original array
'''
a.ravel()  # returns the array, flattened
a.reshape(6,2)  # returns the array with a modified shape
'''
the reshape function returns its argument with a modified shape, whereas the 
ndarray.resize method modifies the array itself
the resize method changes the array itself
'''
# stacking together different arrays
# several arrays can be stacked together along different axes
# for example, array a and array b
c=np.vstack((a,b)) # 两个数组纵向排列成为一个新数组
c=np.hstack((a,b)) # 两个数组横向排列成为一个新数组

# splitting one array into several smaller ones

# copies and views
'''
when operating and manipulating arrays, their data is sometimes copied into 
a new array and sometimes not. this is often a source of confusion for beginners
'''

# not copy at all
a=np.arange(12)
b=a
b is a # b and a are 2 names for the same ndarray object

# view or shallow copy
'''
different array objects can share the same data. the view method creates a new
array object that looks at the same data
'''
c=a.view()
c is a # false
c.base is a # true. c is a view of the data owned by a 
c.shape=2,6 # a's shape does not change
# 这个和没有复制有什么区别啊？ 有区别的，两个数据源相同，但是数组的构造可以不同啊


'''
对于大部分数据分析应用而言，我最关注的功能集中在：
1. 数据整理和清理、子集构造和过滤、转换等快速的矢量化数组运算；
2. 常用的数组算法，排序、唯一化、集合运算等；
3. 高效的描述统计和数据聚合/摘要；
4. 用于异构数据集的合并对齐和关系型数据运算；
5. 将条件逻辑表述为数组表达式；
6. 数据的分组运算（聚合、转换、函数应用等）
'''

'''
创建数组(ndarray)最简单的办法就是使用array函数，它接受一切序列型的对象，然后产生一个
新的含有传入数据的numpy数组
'''

'''
数组很重要，因为它使你不用编写循环即可对数据执行批量运算，大小相等的数组之间的任何算术运算都会将
运算应用到元素级
'''

'''
当你将一个标量值赋值给一个切片时，该值会自动传播到整个选区，跟列表最重要的区别在于，数组
切片是原始数组的试图。这意味着数据不会被复制，视图上的任何修改都会直接反映到源数据上
'''

'''
如果想要得到的是ndarray切片的一份副本而非视图，就需要显式的进行复制操作，如arr[5:8].copy()
以下两种访问方式是等价的 arr[0][2]   arr[0,2]
在多维数组中，如果忽略了后面的索引，则会返回一个维度第一点的ndarray，含有高一级维度上的所有数据
'''

# 数组转置和轴对换
'''
转置是重塑的一种特殊形式，他返回的是源数据的视图，不会进行任何的复制操作，数组不仅有transpose方法。
还有一个特殊的T属性
'''

arr=np.arange(15).reshape(3,5)
arr.T

# 利用数组进行数据处理
points=np.arange(-5,5,.01) # 1000个间隔相等的点
xs,ys=np.meshgrid(points,points)
z=np.sqrt(xs**2+ys**2)
import matplotlib.pyplot as plt

'''
numpy 数组可以进行的运算包括：
1. 数学和统计方法：求和、均值、方差、最小、最大值（索引），元素累积和、累计积
2. 排序，numpy 数组可以通过sort方法就地排序
'''

# 文件的输入输出操作
'''
np.save 和 np.load 是读写磁盘数组数据的两个主要函数，默认情况下，数组是以未压缩的原始
二进制格式保存在扩展名为.npy格式的文件中的
'''
arr=np.arange(10)
np.save('somearray',arr)
a=np.load('somearray.npy')  # 导入数据的时候需要加入后缀名.npy

# 线性代数，矩阵运算
'''
numpy.linalg 中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的方法，
常用的numpy.linalg函数
diag(对角线元素）/dot（矩阵乘法）/trace/det（行列式）/inv/qr/svd/solve
'''

# 随机数生成
'''
numpy.random模块对python内置的random进行了补充，增加了一些用于高效生成多种概率分布的
函数
'''

# 随机漫步
from numpy import random
position=0
walk=[position]
steps=1000
for i in range(steps):
    step=1 if random.randint(-1,1) else -1
    position+=step
    walk.append(position)

# 第五章 pandas入门
'''
pandas 是基于numpy构建的，让以numpy为中心的应用变得更加简单，满足以下需求：
1. 具备按轴自动或显式对齐功能的数据结构
2. 集成时间序列功能
3. 能处理时间序列数据也能处理非时间序列数据的数据结构
4. 灵活处理缺失数据
5. 合并及其他出现在常见数据库中的关系型运算
'''

# pandas 数据结构介绍
'''
使用pandas需要熟悉两个主要数据结构，series和dataframe，为大多数应用提供了可靠的、易于使用
的基础
'''
# series
'''
series是一种类似于一维数组的对象，由一组数据（numpy数据类型）以及一组与之相关的数据标签
、索引组成，仅由一组数据即可产生最简单的series
'''
import pandas as pd
obj=pd.Series([4,7,-5,3])

'''
如果希望创建的Series带有一个可以对各个数据点进行标记的索引：
与普通的numpy数组相比，可以通过索引的方式选取Series中的单个或一组值
还可以将Series看做是一个定长的有序字典，因为它是索引值到数据值的一个映射，可以用在许多原本
需要字典参数的函数中
Series对象本身及其索引都有一个name属性，该属性与pandas其他的关键功能关系非常密切
'''
obj2=pd.Series([1,7,-5,3],index=['a','b','c','d'])

# dataframe
'''
dataframe 是一个表格型的数据结构，含有一组有序的列，每列可以是不同的值类型，既有行索引
也有列索引，可以被看做由series组成的字典，
构建dataframe的办法有很多，最常用的办法是直接传入一个由等长列表或numpy数组组成的字典
'''
import pandas as pd
data={'state': ['ohil','ohio','nevada','nevada'],'year':[2000,2001,2002,2003],
'pop':[1,2,3,4]}
frame=pd.DataFrame(data)
# 如果指定了列序列，则DataFrame的列就会按照制定顺序进行排列
pd.DataFrame(data,columns=['year','state','pop'])
''' 为不在的列赋值会创建出一个新列，关键字del用于删除列 '''

'''
可以输入给DataFrame构造器的数据
二维ndarray、数组列表或元组组成的字典等 p123
'''

# dataframe处理数据的基本功能
'''
pandas 对象的一个重要方法是reindex，其作用是创建一个适应新索引的新对象
'''

# 第六章 数据加载、存储与文件格式
'''
输入输出通常可分为几个大类：读取文本文件和其他更高效的磁盘存储格式，加载数据库中的数据，
利用web api 操作网络资源
'''

'''
pandas 提供了一些用于将表格型数据读取为dataframe对象的函数，
read_csv: 从文件、URL、文件型对象中加载带分隔符的数据，默认分隔符为逗号
read_table：从文件、URL、文件型对象中加载带分隔符的数据，默认分隔符为制表符
read_fwf：读取定宽列格式数据
read_clipboard： 读取剪贴板中的数据，可以看做read_table的剪贴板版，在将网页转换为表格时很有用
类型推断是这些函数中最重要的功能之一，也就是说你不需要指定列的数据是数值、整数还是字符串，
日期和其他自定义类型的处理需要多花点功夫
'''

'''
读取microsoft excel 文件
pandas的ExcelFile类支持读取存储在excel中的表格型数据，由于ExcelFile用到了xlrd和openpyxl包，
所以需要先安装上述两个。通过传入一个xls或xlsx文件的路径即可创建一个ExcelFile实例：
xls_file=pd.ExcelFile('data.xls')
存放在某个工作表中的数据可以通过parse读取到dataframe中：
table=xls_file.parse('Sheet1')

大量的数据会取自数据库中，python也有相应的方法
'''

# 第七章 数据归整化：清理、转换、合并、重塑
# 合并数据集
'''
pandas.merge可根据一个或多个键将不同dataframe中的行连接起来
pandas.concat可以沿着一条轴将多个对象堆叠到一起

替换值：利用fillna方法填充缺失数据可以看做值替换的一种特殊情况，虽然map方法可以用于修改
对象的数据子集，而replace则提供了一种实现该功能的更简单、灵活的方式
'''
data.replace(-999,np.nan)
# 如果希望一次性替换多个值，可以传入一个由待替换值组成的列表以及一个替换值
data.replace([-999,-1000],np.nan)
# 如果希望对不同的值进行不同的替换，则传入一个由替换关系组成的列表即可
data.replace([-999,-1000],[np.nan,0])

# 第八章 绘图和可视化
'''
matplotlib 是一个用于创建出版质量图表的桌面绘图包，为python构建一个matlab式的绘图接口，
matplotlib还有许多插件工具集，如用于3D图形的mplot3d以及用于地图和投影的basemap
'''

'''
matplotlib 的图像都位于Figure对象中，不能通过空Figure绘图，必须用add_subplot创建一个
或多个subplot才行
'''
import matplotlib.pyplot as plt
from numpy.random import randn
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
'''
如果这时发出一条绘图命令，matplotlib就会在最后一个用过的subplot上进行绘制，
'''
plt.plot(random.randn(50).cumsum().'k--')


# pandas 中的绘图函数
'''
Series和DataFrame都有一个用于生成各类图表的plot方法
'''

# 第11章 金融和经济数据应用






















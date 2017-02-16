# -*- coding: utf-8 -*-
# 列表(list)和元组(tuple)是python中两种最原始的数据结构，两者的差别在于列表可以修改，元组不能。

# list 列表
# 练习1，根据指定的年月日以数字形式打印出日期
months=['January','February','March','April','May','June','July' \
'August','September','October','November','December']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=input('Year:')
month=input('Month:')
day=input('Day:')
year_number=int(year)
month_number=int(month)
day_number=int(day)
month_name=months[month_number-1]

print(year+' '+month_name+' '+day+endings[day_number-1])
# 我还没有弄明白输入输出的方法


# 分片索引
numbers=[1,2,3,4,6,7,8]
print(numbers[2:5])
# 分片索引时第一个索引包括，最后一个索引不包括

# add new items to the end of list
numbers.append(100)
# delete some items in the list
numbers[3:5]=[]

# get the length of a list
len(numbers)


# more control flow tools
# if statements
a=int(input('please input a number: '))
if a>0:
    print('positive')
elif a==0:
    print('zero')
else:
    print('negative')

# for statements
# measure some strings
examples=['subway','programmer','apple','banana']
for a in examples[:]:
    print(a,len(a))

# the range function
# if you need to iterate over a sequence of numbers
for i in range(5):  # 0 1 2 3 4
    print(i)
# in many ways the object return by range() as if it is a list, but in fact
# it isn't. t is an object which returns the successive items of the desired
# sequence when you iterate over it, but it doesn’t really make the list, 
# thus saving space. to get a list, you need to do like this:
    a= list(range(1,50,2))

# break and continue statements, and else clause on loops
# find a prime number fron 1 to 100
upper=100
for i in range(1,100): # range do not contain an item of 100, the last one is 99
    for j in range(2,i):
        if i%j==0:
            print(i,'=',j,'*',i/j)
            break # break a loop for or while, not if
    else:
        print(i,'is a prime number')

# continue statement
for i in range(1,10):
    if i%2==0:
        print('find a even number',i)
        continue; # 此时直接跳过for中的下一语句，进入下一个循环了
    print('find a odd number')
    
# defining functions
def fib(n): # define a fibonacci series up to n
    a,b=0,1
    while(a<n):
        print(a,end=' ')
        a,b=b,a+b
        
# you can use a function like these
fib(100)
f=fib
f(100)

# defint a function which returns a list
def fib(n):
    a,b=0,1
    result=[]
    while(a<n):
        result.append(a)
        a,b=b,a+b
    return result

# python 的代码对齐规则是什么？
# 同一级别的代码应保持相同的缩进

# more on defining functions
# default argument values
def ask_ok(prompt,retries=4,reminder='please try again'):
    while(True):
        # print('hahah') 运行的时候为什么没有这一句
        ok=input(prompt)
        if ok in ('y','yes','ye'): # 这个东西和list有什么区别？
            return True
        elif ok in ('no','n','nop','nope'):
            return False
        retries=retries-1
        if(retries<0):
            raise ValueError('invalid user response')
        print(reminder)
# 在给function传入默认参数的时候，必须输入字段名

# keyword arguments
def cheeseshop(kind,*arguments,**keywords):
    print('do you have any',kind,'?')
    print("I'm sorry,we are all out of",kind)
    for arg in arguments:
        print(arg)
    print('_'*40)
    keys=sorted(keywords.keys())
    for kw in keys:
      print(kw,':',keywords[kw])  
    
cheeseshop('Limburger',"It's very runny,sir","It's true",shopkeeper="Michael"\
,client="John Cle",sketch="Cheese shop sketch")    
 # 有了*arguments 和 **arguments 函数可以接收字典类型数据作为参数   
    
    
# arbitrary aurument lists
# these arguments will be wrapped up in a tuple.
def concat(*args,sep="/"):
    return sep.join(args)

concat("earth","mars","venus")
    
# unpacking argument lists
# when the arguments are already in a list or tuple but need to be
# unpacked for a funciton call requiring separate positional arguments    
list(range(3,6))
args=[3,6]
list(range(*args))
# in the same fashin,dictionaries can deliver keyword arguments with **    

# data structures
# list comprehension
''' list comprehension provide a concise way to creast lists.Common applications'''
# traditional ways to create a list of squares
squares=[]
for i in range(10):
    squares.append(i**2)
# but now we can create it like this
squares=list(x**2 for x in range(10) )
''' a list comprehension cosists of brackets containing an expression followed    
by a for clause, then zero or more for or if clauses. the result will be a new   
list resulting from evaluating the expression in the context of the for and if
clauses which follow if '''
[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
    
vec = [-4, -2, 0, 2, 4]  
# create a new list with the values doubled  
[x*2 for x in vec]  
# filter the list to exclude negative numbers   
[x for x in vec if x>=0] 
# apply a function to all the elements
[abs(x) for x in vec]    
# create a list of 2-tuples like (number, square)   
[(x,y) for x in vec if x>0 for y in vec if y<0] 



# tuples and sequences
# there is also another standard sequence data type: the tuple
t=12345,34,'hello'
# tuples can be nested
u=t,(1,2,3,4,5)
# tuples are immutable, but they can contain mutable objects
v=([1,2,3],[4,5,6])
v[1][2]=100
''' a special problem is the construction of tuples containing 0 or 1
items: the syntax has some extra quirks to accommodate these.
Empty tuples are constructed by an empty pair of parentheses; a tuple with one
item is constructed by following a value with a comma '''



''' sets
a set is an unordered collection with no duplicate elements.
basic uses include membership testing and eliminating duplicate entries
curly braces of the set() function can be used to create sets. but to create
an empty set you have to use set(), not {}; the latter creates an empty dictionary '''
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)  # duplicates will be removed
a=set('dkfdk') # and that will be unique letters in a, not a string
# similarly to list comprehensions, set comprehensions are also supported
a={x for x in 'dkjfdk' if x not in 'df'}


''' 
dictionaries
unlike sequences, which are indexed by a range of numbers, dictionaries
are indexed by keys, which can be any immutalbe type, strings and numbers
can always be keys
it is best to think of a dictionary as an unordered set of key: value paires
with the requirement that the keys are unique.
the main operations on a dictionary are storing a value with some key and 
extracting the value given the key
 '''
 # create a dictionary
tel={'jack':4098,'sape':4139}
tel['irv']=4124
# the dict() constructor builds dictionaries directely from sequence of key-value pairs
dict([('sape',4139),('guido',4127),('jack',4098)])
# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
{x:x**2 for x in(2,4,6)}
# when looping through dictionaries, the key and corresponding value can be
# retrieved at the same time using the items() methond
knights={'galla':'the pure','robin':'the brave'}
for k,v in knights.items():
    print(k,v)
''' 
to loop over two or more sequences at the same time,the entries can be
paired with the zip() function
'''
questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q, a))  # 这是什么玩法，没见过

'''
more on conditions
the conditions used in while and if statements can contain any operators,
not just comparisons.
the comparison operators in and not in check whether a value occurs in a sequence
the operators is and is not compare whether two objects are the same object
'''

''' 
modules
python has a way to put definitions in a file and use them in a script or 
an interactive instance of the interpreter. such a file is called a module;
definitions from a module can be imported into other modules or into the main module.

a module is a file containing python definitions and statements. the file name is 
the module name with the suffix.py appended.
within a module, the module's name is a variable as the value of the global variable
__name__
'''
# an example for module
'''
create a file called fibo.py in the current directory with the following contents:
'''
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
'''
when enter the python interpreter and import this module with 
import fibo
then you get an access to the functions within the module
'''
fibo.fib(1000)
fibo.fib2(1000)
fibo.__name__

'''
if you intend to use a function frequently, you can assign it to a local name
'''
fib=fibo.fib
fib(500)

# more on modules
'''
a module can contain executable statements as well as funtion definitions.
these statements are intended to initialize the module. they are executed only the
first time the module name is encountered in an import statement.
modules can import other modules
'''

'''
there is a variant of the import statement that imports names from a module directly
into the importing module's symbol table
'''
# import specified names
from fibo import fib,fib2
# or
from fibo import *


'''
the module search path
when a module name spam is imported, the interpreter first searches for a 
built-in module with that name. if not found, it then search for a file in a list
of directories given by the variable sys.path which will be initialized
'''

'''
standard modules
described in a separate document, the python library reference
the variable sys.path is a list of strings that determines the search path for modules
'''
# modify the path
import sys
sys.path.append('/ufs/guido/lib/python')

# the dir() function
'''
the built-in function dir() is used to find out which names a module defines.
it returns a sorted list of strings
dir() does not list the names of built-in functions and variables. if you want a list of
those, they are defined in the standard module builtins
'''

'''
packages
packages are a way of structuring python's module namespace by using "dotted
module names". for example, the module name A.B designates a submodule named B 
in a package named A.
the __init__.py files are required to make python treat the directories as con-
taining packages. in the simplest case, __init__.py can just be an empty file,but
it can also execute initialization code for the package or set the __all__ variable.
'''
import sound.effects.echo
'''
this loads the submodule sound.effects.echo. it must be referenced with its full name
'''
sounds.effects.echo.echofilter(input,output,delay=.7,atten=4)
# an alternative way of importing the submodule is
from sound.effects import echo
# this also loads the submodule, and makes it available without its package prefit
# so it can be used as follows:
echo.echofilter(input,output,delay=.7,atten=4)
# another variation is to import the desired function or variable directly
from sound..effects.echo import echofilter
# this makes the function directly available


# input and output
# basic usage of the str.format() method look like this
print('we are the {} who say "{}!"'.format('knights','Hi'))
# we are the knights who say "Hi!"
'''
the brackets and characters within them are replaced with the objects passed 
into the str.format() method. a number in the brackets can be used to refer to
the position of the object passed into the str.format() method
'''
print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam

'''
if keyword arguments are used in the str.format() method, their values are 
referred to by using the name of the argument
'''
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# positional and keyword arguments can be arbitrarily combined
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

'''
an optional ':' and format specifier can follow the field name.
'''
import math
print('the value of PI is approximately {0:.3f}'.format(math.pi))
'''
passing an integer after the ':' will cause that field to be a minimum number of
characters wide, which is useful for making tables pretty.
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print('{0:10}===>{1:10}'.format(name,phone))


# reading and writing files
'''
open() returns a file object, and is most commonly used with 2 arguments:
open(filename,mode)
filename is a string containing the filename. mode is another string containing
a few characters describing the way in which the file will be used.
'r'-->only be read  'w'-->only writing  'a'-->appending 'r+'-->both reading and writing
default value 'r'
'''
f=open('workfile','w')


# methods of file objects
# the rest of the examples in this section will assume that a file object f created
with open('workfile','r') as f:
    read_data=f.read()

# saving structured data with json
# errors and exceptions
# 2 distinguishable kinds of errors: syntax errors and exceptions
# handling exceptions
while True:
    try:
        x=int(input('please enter a number: '))
        print('the number you just input is: ',x)
        break
    except ValueError:
        print('no valid number. try again')
'''
the try statement works as follows:
1. try clause(the statements between the try and except) is executed.
2. if no exception occurs, the except clause is skipped and execution is skipped
3. if an exception occurs during execution of the try clause, the rest of the 
clause is skipped. then if its type matches the exception named after the except
keyword, the except clause is executed
4. if an exception occurs which does not match the exception named in the except
clause, it is passed on to outer try statements; if no handler is found, it's 
an unhandled exception and execution stops with an error message
'''
import sys
try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
 except OSError as err:
    print("OS error: {0}".format(err))
 except ValueError:
    print('could not convert data to an integer')
 except:
     print('unexpected error:',sys.exc_info()[0])
     raise

'''
the try...except statement has an optional else clause, it is useful for code
that must be executed if the try clause does not raise an exception.
'''
for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()


# classes
'''
python scopes and namespaces
a namespace is a mapping from names to objects. 
attribute is a name following a dot--z.real, real is an attribute of the object
attributes may be read-only or writable.
a scope is a texual region of a python program where a namespace is directly accessible
'''

# a first look at classes
class myclass:
    i=123
    def f(self):
        return 'hello'
# define a class
x=myclass()
'''
the instantiation operation creats an empty object. many classes like to create 
objects with instances customized to a specific initial state, therefore a class
may define a special method named __init__()
'''
def __init__(self):
    self.data=[]

'''
of course, the __init__() method may have arguments for greater flexibility. in
that case, arguments given to the class instantation operator are passed on to __init__
'''
class complex110:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=complex110(3.4.5)
#  x.r=3 x.i=4.5

# instance objects
'''
the only operations understood by instance objects are attribute references.
there are 2 kinds of valid attribute names, data attributes and methods
'''
# correct design of the class should use an instance variable instead:
class dog:
    def __init__(self,name):
        self.name=name
        self.tricks=[]
    def addtricks(trick):
        self.tricks.append(trick)
d=dog('D')
d.add_trick('roll over')

# inheritance
# the syntax for a derived class definition looks llke this:
class derivedclass(baseclassname):
    statements ...
    
# multiple inheritance
class derivedclass(base1, base2, base3):
    statements ...

# private variables

# generators
'''
generators are a simple and powerful tool for creating iterators, they're written
like regular functions but use yield statement whenever they want to return data
'''
def reverse(data):
    for index in range(len(data)-1.-1,-1):
        yield data[index]


# brief tour of the standard library

# operating system interface
# the os module provides dozens of functions for interacting with the operating system
import os
os.getcwd()  # return the current working directory
'''
the built-in dir() and help() functions are useful as interactive aids for working
with language modules
'''
import os
dir(os)  # return a list of all module functions
help(os) # returns an extensive manual page created from the module's docstrings


# mathematics
'''
tha math module gives access to the underlying C library functions for floating point math
'''
import math
math.cos(math.pi/4)
math.log(1024,2)

'''
the random module provides tools for making random selections
'''
import random
random.choise(['apple','pear','banana'])  # apple
random.sample(range(100),10)  # sampling without replacement  无放回抽样？
random.random() # random float
random.randrange(6) # random integer chosen from range(6)

'''
the statistic module calculates basic statistical properties(mean,median,var) of numeric data
'''
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# the scipy object has many other modules for numerical computations

# internet access
'''
there are a number of modules for accessing the internet and processing internet
protocols. 2 of the simplest are urllib.request for retrieving data from URLs and 
smtplib for sending mail:
'''
from urllib.request import urlopen
while urlopen('http://nba.hupu.com') as response:
    for line in response:
        line=line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line: # look for Eastern time
           print(line)

# dates and times
'''
the datetime module supplies classes for manipulating dates and times for in both simple
and complex ways.
'''
from datetime import date
now=date.today()
birthday=date(1990,11,14)
age=now=birthday
age

# performance measurement
# the timeit module quickly demonstrates a modest performance advantage
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# output formatting
'''
the reprlib module provides a version of repr() customized for abbreviated displays
of large or deeply nested containers:
'''

# managing packages with pip
'''
once you've activated a virtual environment, you can manage packages using a program
called pip
'''










































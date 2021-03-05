import threading,time


# lst = list(range(20))

def test(item):
	time.sleep(0.1)
	print(str(item)+'\n',end='') # 可能是线程运行太快，以至于默认的print方法的'\n'，打印太慢，参数都同时打印在了同一行，故修改了默认结束参数为end=''


def thread_test():
	t_list=[]
	for i in range(6):
		t=threading.Thread(target=test,args=(i,))
		t.start()
		# t.join() # 如果这样写，子线程会按顺序执行。
		t_list.append(t)

	for i in t_list:
		i.join() # 用来回收结束的子线程，只有子线程都结束了才能运行后面的代码，否则主线程可能在子线程运行完之前就结束了，会产生孤儿进程

	print('主线程结束')
# thread_test()

# ***************************************************************************************
a=[12345678,123456789,88888888,7777777,999999999]
b= filter(lambda x: len(str(x)) < 9 and len(str(x)) > 7, a)
print(list(b))

# ***************************************************************************************
import os
# print(os.popen("pip list").read())

print(time.strftime('%Y-%m-%d %H:%M:%S'))

# ***************************************************************************************
def for_test():
	for item in range(10):
		pass
	print(item)

# for_test()
# ***************************************************************************************
from pandas import Series,DataFrame
import pandas as pd
data = Series(list(range(1,6)),index=['a','b','c','d','e']) # 参数可传列表
# print(data)
dac1={'a':'111',2:'bbb','c':333}
data1 = Series(dac1) # 参数也可传字典
# print(data1)
data2=DataFrame({'A':[123,'str'],'b':['456',666]}) # 参数中的列表长度必须相等
# print(data2)



# ***************************************************************************************
d = {'lily':25, 'wangjun':22, 'John':25, 'Mary':19}
# print(d.items())
# print(sorted(d.items(),key=lambda x:x[1],reverse=True)) # 根据年龄排序，返回列表形式。
a=list(range(1,6))
a.sort(reverse=True) # sort方法不能对字典操作，只能对列表类型排序
# print(a)
# ***************************************************************************************
def square(x) :            # 计算平方数
    return x ** 2

# map函数返回迭代器
eg1 = map(square, [1,2,3,4,5])  # 计算列表各个元素的平方   
# print(list(eg1))   # >>> [1, 4, 9, 16, 25]
eg2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数   
# print(list(eg2))    # >>> [1, 4, 9, 16, 25]
# 提供了两个列表，对相同位置的列表数据进行相加
eg3 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) 
# print(list(eg3))    # >>> [3, 7, 11, 15, 19]
# ***************************************************************************************
print(set([1,2,3]) & set([1,1,6]))   #  & -> and    找到两个列表中同时存在的元素，必须将列表转换为集合
print(set([1,2,3]) | set([1,1,6,5])) #  | -> or		找到两个列表的并集
print(set([1,2,3]) ^ set([1,1,6,5])) #  ^ -> 		找到两个列表中除了交集剩下元素的并集

# ***************************************************************************************
import requests,time
import platform
import datetime


if platform.system()=='Windows':
    print(platform.system())


print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%H'))
print(time.strftime('%H'))

# ***************************************************************************************
import sys
# CMD窗口：C:\Users\Yang志>python C:\Users\Yang志\Desktop\123.py 我是参数1 我是参数2
print(sys.argv) # 即后续cmd中需要传入的参数列表(多个参数要用空格隔开) ---> ['C:\\Users\\Yang志\\Desktop\\123.py', '我是参数1', '我是参数2']
print(sys.argv[0]) # 即要执行的文件名
# print(sys.argv[1]) # 即参数的字符串，如果不传参这里会报错，索引越界
print(len(sys.argv)) # --- > 3

# ***************************************************************************************
import sys
import os

print(os.path.dirname(__file__)) # 获取当前文件的绝对路径
print(os.path.basename(__file__)) # 获取当前脚本的文件名
print(sys.path[0])  # 获取当前文件的绝对路径，也有可能返回文件名？？
path=sys.path[0]
print(os.path.dirname(path)) # path的目录，即上一级目录
print(sys.path)
# print(os.listdir(os.path.dirname(__file__)))

try:
	# sys.argv[1]
	print('this is try')
except Exception as e:
	# raise 'this is except'
	print('this is except')
else:
	print('this is else')
finally:
	print('this is finally')

# ******************************* 装饰器 ************************************************

# 普通装饰器
def fuc(fuc): # decortor
	def inner(*args): # wrapper
		print('我是装饰内容')
		return "被装饰内容:"+fuc(*args)
	return inner
@fuc
def fuc2(a,b):
	return "{},{}".format(a,b)

c=fuc2(12345,6789)
print(c)

# 可传参装饰器
def tag(name):
	def add_name(fuc): # decorator
		def inner(*args):# 真正的装饰器wrapper
			return "<{0}>{1}</{0}>".format(name,fuc(*args))
		return inner
	return add_name
@tag('h1')
def text(str):
	return str
result = text('这是正文')
print(result)


print([item for item in os.listdir(os.path.dirname(__file__)) if os.path.isfile(item)])

# *************************** 数字转大写字母 *************************************
def getChars(length):
    return [getChar(index) for index in range(length)]

def getChar(number):
    factor, moder = divmod(number, 26) # 26 字母个数
    modChar = chr(moder + 65)          # 65 -> 'A'
    if factor != 0:
        modChar = getChar(factor-1) + modChar # factor - 1 : 商为有效值时起始数为 1 而余数是 0
    return modChar

# print(getChar(25)+str(1))

# ******************************************************************************
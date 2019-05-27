from pandas import Series, DataFrame
import pandas as pd

# pandas简介：
# Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一

# pandas 会对数据对齐显示，灵活处理缺失数据，类似sql语句的连接操作
# Series对numpy的array进行了封装，对所有的数值添加了一个索引
# Series是对一维数组进行的操作

# pandas的安装：
# 需要在terminal 中安装 pip3 install pandas

obj = Series([4, 5, 6, -7])
print(obj)

print('index:', obj.index)
print('values,', obj.values)

obj2 = Series([4, 7, -5, 3], index=['a', 'c', 'd', 'b'])
print(obj2)
obj2['d'] = 0
print(obj2)

print('f' in obj2)

sdata= {'beijing' :100000, 'shanghai':200000, 'tianjin':'300000'}
obj3 = Series(sdata)
print(obj3)
# 改变索引
obj3.index=['bj', 'sh', 'tj']
print(obj3)
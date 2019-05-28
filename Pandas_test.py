from pandas import Series, DataFrame
import pandas as pd

# pandas简介：
# Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一
# pandas 会对数据对齐显示，灵活处理缺失数据，类似sql语句的连接操作

# pandas的安装：
# 需要在terminal 中安装 pip3 install pandas

# Series对numpy的array进行了封装，对所有的数值添加了一个索引
# Series是对一维数组进行的操作
print('===============Series==================')

obj = Series([4, 5, 6, -7])
print(obj)

print('index:', obj.index)
print('values,', obj.values)

# 手动指定索引
obj2 = Series([4, 7, -5, 3], index=['a', 'c', 'd', 'b'])
print('obj2: \n', obj2)
obj2['d'] = 0
print('obj2 new: \n',obj2)

print('f' in obj2)

#  将字典转化为series，字典的key会变成series的索引
sdata= {'beijing' :100000, 'shanghai':200000, 'tianjin':'300000'}
obj3 = Series(sdata)
print(obj3)
# 改变索引
obj3.index=['bj', 'sh', 'tj']
print(obj3)

print('===============Dataframe==================')
# Dataframe对二维三维数组进行操作

data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
# 支持按顺序显示
frame2 = DataFrame(data,columns=['year', 'city', 'pop'])
print(frame2)

print(frame2['city'])
print(frame2.city)
# 给二维数组增加新列
frame2['gdp'] = 7.0
print(frame2)

frame2['isCapital'] = frame2.city == 'beijing'
print(frame2)

# 另一种为dataframe赋值的方式是字典的嵌套
pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }

frame3 = DataFrame(pop)

print(frame3)
# 行和列的互换，也叫行列式的转置
print(frame3.T)

# reindex---dataframe更有用的功能

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])

# obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'])
# 如果索引对应的值为Nan，会给数据清洗带来影响，所以给空值一个手动填充
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

print(obj5)
# 如果是字符串，不适合用fill_value =0 进行填充，可以使用method
# ffill 用前一个索引对应的值进行填充，bfill用后一个索引对应的值进行填充
obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj6.reindex(range(6),method='ffill'))
print(obj6.reindex(range(6),method='bfill'))

# 有一些值无法进行填充和补全，那就需要进行删除
from numpy import nan as NA
data1 = Series([1, NA, 2])
print(data1.dropna())

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])
# 删除整行都是缺失值
print(data2.dropna(how = 'all'))

# 删除整列都是缺失值的
data2[4] = NA # 添加一行NaN的测试列
print(data2)
print(data2.dropna(axis = 1, how= 'all'))

data2.fillna(0)
# 下面的写法只能修改data2.fillna这个副本，如果想要修改data2,需要加上inplace = True
# print('fillna:',data2.fillna(0)
print('fillna:',data2.fillna(0, inplace=True))
print('data2:', data2)

print('===============层次化索引==================')
import numpy as np
# 层次化索引，可以根据索引的层次来提取数据
data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

print(data3)
# print(data3['b'])
# print(data3['b':'c'])

# 将Series数据转换成dataFrame形式的数据
print(data3.unstack())
# 再转化回series
print(data3.unstack().stack())





# 相关链接
# http://pandas.pydata.org/9
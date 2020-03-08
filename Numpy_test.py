# 几个步骤：数据的采集，预处理，清洗，建模，测试

# Numpy简介：
# NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
# Numpy内部解除了CPython的GIL（全局解释器锁），运行效率极好，是大量机器学习框架的基础库！
# 关于GIL请参考博客：http://www.cnblogs.com/wj-1314/p/9056555.html

# numpy库用于高性能科学计算和数据分析，是常用的高级数据分析库的基础包
# numpy是进行数据预处理的非常重要的库，基于C语言开发的，处理数据非常高效

# NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：
# . 一个强大的N维数组对象 ndarray
# . 广播功能函数
# . 整合 C/C++/Fortran 代码的工具
# . 线性代数、傅里叶变换、随机数生成等功能

# NumPy的优点：
# 对于同样的数值计算任务，使用NumPy要比直接编写Python代码便捷得多；
# NumPy中的数组的存储效率和输入输出性能均远远优于Python中等价的基本数据结构，且其能够提升的性能是与数组中的元素成比例的；
# NumPy的大部分代码都是用C语言写的，其底层算法在设计时就有着优异的性能，这使得NumPy比纯Python代码高效得多
# 当然，NumPy也有其不足之处，由于NumPy使用内存映射文件以达到最优的数据读写性能，而内存的大小限制了其对TB级大文件的处理；此外，NumPy数组的通用性不及Python提供的list容器。因此，在科学计算之外的领域，NumPy的优势也就不那么明显



# numpy的安装：
# 需要在terminal 中安装 pip3 install numpy
# 注意：安装前先更新pip3   https://pip.pypa.io/en/stable/installing/#upgrading-pip
# pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。
# 注意：mac下是pip3,不是pip
# 命令行：pip3 install --upgrade pip
# pycharm 中需要在配置中添加numpy

import numpy as np

# np的array 计算效率要远远高于python的array
# 将列表转换为数组
arr1 = np.array([2, 3, 4])
print(arr1)
# 数组元素类型
print('数组元素类型dtype: ', arr1.dtype)
# Numpy查看数组属性
print('数组属性size: ', arr1.size)
# 数组形状
print('数组形状shape: ', arr1.shape)
# 数组维度
print('数组维度ndim:', arr1.ndim)


arr2 = np.array([1.2 , 2.3, 3.4])
print(arr2 , 'arr2的类型是：', arr2.dtype)

print(arr1 + arr2)

print(arr2 * 10)
print('对比下普通数组的*')
arr_t = [1,2,3]
print('arrt:', arr_t * 10)

# 多于一个维度
data = [[1,2,3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3)
print('arr3的类型是：', arr3.dtype)

# 返回特定大小，以0填充的新数组。
print(np.zeros(10))
# 一个3行5列的矩阵
print(np.zeros((3,5)))
# 返回特定大小，以1填充的新数组
print(np.ones((4,6)))

# 它创建指定形状和dtype的未初始化数组。它使用以下构造函数：numpy.empty(shape, dtype = float, order = 'C')
# 2*3的空值矩阵，为了安全性，会填入随机数
print('empty:', np.empty((2,3)))

# 最小维度
arr4 = np.array([1, 2, 3, 4, 5], ndmin=2)
print('最小维度arr4:' ,arr4)
# [[1 2 3 4 5]]

# dtype 参数
arr5 = np.array([1, 2, 3], dtype=complex)
print(arr5)

print('====================')
# 基本切片是Python中基本切片概念到n维的扩展，通过start，stop和step参数提供给内置函数的slice函数来构造一个Python slice对象，此slice对象被传递给数组来提取数组的一部分。
arr6 = np.arange(10)
print(arr6)
# 对索引之间的元素进行切片
print('数组的切片原值：',arr6[5:8])
# 修改原数组
arr6[5:8] = 10
print('数值修改后：', arr6)
# 不修改原数组
arr_slice = arr6[5:8].copy()
# slice中全部数值都需要修改，要加上[:]
arr_slice[:] = 15

print(arr6)
print(arr_slice)

# Numpy的应用：
# NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。
# SciPy 是一个开源的 Python 算法库和数学工具包。
# SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。
# Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。它为利用通用的图形用户界面工具包，如 Tkinter, wxPython, Qt 或 GTK+ 向应用程序嵌入式绘图提供了应用程序接口（API）


# 相关链接：
# 具体使用，函数，属性：https://www.cnblogs.com/wj-1314/p/9722794.html
# NumPy 官网 http://www.numpy.org/
# NumPy 源代码：https://github.com/numpy/numpy
# 比较全面的Numpy中文手册：https://www.runoob.com/numpy/numpy-tutorial.html

# SciPy 官网：https://www.scipy.org/
# SciPy 源代码：https://github.com/scipy/scipy
# Matplotlib 官网：https://matplotlib.org/
# Matplotlib 源代码：https://github.com/matplotlib/matplotlib


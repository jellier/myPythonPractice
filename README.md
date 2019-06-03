## 一些python的练习
### different from js:
> if 后不需要加（）

> json格式{'x':1,'y':2}在python里面叫字典

### 待解决的疑问：
##### filter lambda
##### with open的使用？
##### re库的用法？

### 文件操作的代码
> file_op.py,主要是read,writ,close的使用
> seek,readline(s)也是经常用到的方法

### 异常处理
<pre><code>
try:
   <监控异常>
except Exception:
    <异常处理代码>
finally:
    <无论异常是否发生都执行>
</code></pre>
raise可以用来自定义错误提示信息
<pre><code>
try:
    raise NameError('my custom error')
except NameError:
    print('error')
</code></pre>
### 函数
#### 常用操作
<pre><code>
def funcName:
    ****
    return ***
</code></pre>
#### 可变长参数
#### 迭代器和生成器
#### lambda
<pre><code>
def func(x):
    return x+1
等同于
lambda x : x+1
</code></pre>

### 内建函数
> filter()

> map()

> reduce() 需要使用"from functools import reduce"

> zip()

###模块的使用
> import 模块名
> import 模块名 as 缩略名
> from 模块名 import 函数名
 <pre><code>
import time
import time as t
form time import sleep
</code></pre>
### PEP8
> PEP8的规范：https://www.python.org/dev/peps/pep-0008/

> 也在终端使用pip3安装autoPEP8，然后在pycharm中的扩展工具中加入autopep8
<pre><code>
pip3 install autopep8
</code></pre>

### 类
#### --面向过程和面向对象


### 标准库

### 机器学习库 && 数据分析
#### 关于numpy 与pandas的关系：

> 当Python开始涉足数据分析领域时，其便渐渐形成了与R语言分庭抗礼的趋势。而在这股势力中，其主角及成员便是NumPy、pandas、matplotlib以及scipy

> 对于由于Python自身的动态语言特性而带来的运行速度方面的损失，NumPy已经做了相当程度的优化，可以对大数组的数据进行高效处理。优化包括NumPy是在一个连续的内存块中存储数据，独立于其他Python内置对象，如此便可以加速数据索引的速度。其次，NumPy调用了大量的用C语言编写的算法库，使得其可以直接操作内存，不必进行Python动态语言特性所含有的前期类型检查工作，从而大大提高了运算速度。最后，NumPy所有独有的可以在整个数组上执行复杂的计算也能够大幅提高运算效率（基于NumPy的算法要比纯Python快10到100倍，甚至会快更多）。

> 对于Python在大数据处理方面（数G甚至几十上百G）的捉襟见肘，经过合理的优化，Python处理几个G的数据绰绰有余，至于几十G也勉强可以，而上百G的数据这就算是Hadoop与Spark系列的任务，不是Python的NumPy与pandas可以应付的，也不是R语言某个第三方包可以处理的。

> NumPy除了在相当程度上优化了Python计算过程，其自身还有较多的高级特性，如指定数组存储的行优先或者列优先、广播功能从而快速的对不同形状的矩阵进行计算、ufunc类型的函数可以使得我们丢开循环而编写出更为简洁也更有效率的代码、使用开源项目Numba编写快速的NumPy函数，而Numba则是可以利用GPU进行运算的。


> 虽然NumPy有着以上的种种出色的特性，其本身则难以独支数据分析这座大厦，这是一方面是由于NumPy几乎仅专注于数组处理，另一方面则是数据分析牵涉到的数据特性众多，需要处理各种表格和混杂数据，远非纯粹的数组（NumPy）方便解决的，而这就是pandas发力的地方。


> pandas 这个名称来源于panel data（面板数据），从而可见其要处理的数据是多维度的而非单维度。pandas 含有使数据清洗和分析工作变得更快更简单的数据结构与操作工具。经常是和其他工具一起使用，如数值计算工具NumPy和SciPy，分析库statsmodels与scikit-learn，以及数据可视化库matplotlib。其中NumPy则是构建pandas的基础，后者大量借鉴了NumPy编码风格。

> 如果用做一餐饭来比喻，pandas于处理数据方面的功用则相当于将米洗好，将菜摘好洗好以及切好的过程，至于入锅添油加醋，锅铲捣腾，做成一道菜则是依靠statsmodels、scikit-learn和matplotlib的功能。
#### Numpy
> 专注于数组处理
> Numpy是以矩阵为基础的数学计算模块，纯数学。
#### Pandas
> Series 和 Dataframe
> 时间序列类函数，可以说是pandas让处理时间序列数据变得得心应手

> Pandas提供了一套名为DataFrame的数据结构，比较契合统计分析中的表结构，并且提供了计算接口，可用Numpy或其它方式进行计算。
#### matplotlib
> Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。
#### scipy
> Scipy基于Numpy，科学计算库，有一些高阶抽象和物理模型。比方说做个傅立叶变换，这是纯数学的，用Numpy；做个滤波器，这属于信号处理模型了，在Scipy里找。


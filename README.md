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
#### 面向过程和面向对象

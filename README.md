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

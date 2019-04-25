# 函数的使用方法,基本功能及常用函数
# 可参考官方文档：https://docs.python.org/3/howto/functional.html

# 参数的使用方法
def functest(a, b, c):
    print('a = %s' %a)
    print('b = %s' %b)
    print('c = %s' %c)

functest( 1 , 2, 3)
functest(c=1, a=2, b=3)
print('======')

# 可变长参数，*后面的参数非必填项
def howlongthisfuc(firstarg, *others):
    argLens = 1 + len(others)
    print('这个函数共有 %s 个参数' %argLens )

howlongthisfuc('abc','adfa','adfasdf','afsdfadffa')

# iter() means iterator 迭代器,一次只输出一个值
# iter() 和 next()的使用方法
# 相当于for in
print('======')
list1 = [1, 2, 3]
its = iter(list1)
print(next(its))
print(next(its))
print(next(its))
# print(next(its))  #超出列表的长度会报错
print('======')
for i in range(10,20,2): #此处步长为2，只可以整数，不支持浮点
    print(i)

# range不支持浮点数的步长
# 用生成器定义一个支持浮点数的range
# 带yield的函数我们称为迭代器，这种函数返回一个固定的对象，叫迭代器对象，
# 它和return的最大区别是，如果需要返回无限序列，return会产生一个巨大的列表，很明显存在内存限制问题，所以引入了yield返回一个固定长度的值
def floatrange(start,stop,step):
    x = start
    while x < stop:
        # 此处如果没有yield，会将所有x<stop的值一次性返回
        # yield的作用是需要一个数据时才产生一个，而不是把数据一次性存入内存，相当于把数据提前定义成列表来使用要极为节省系统资源
        # 一般访问生成器要使用next()方法，也可以使用list方法一次性取出，但是一次性读取出来就和列表一样了，失去了自身的优势
        yield x
        x += step
for i in floatrange(10 ,20, 0.5):
    print(i)
print('======')

for i in floatrange(10 ,20, 0.2):
    print(i)
# 步长换成0.2，结果变成10/10.2/10.3999999....
# 出现这样的结果是因为浮点数缺乏精确性导致的，不止在python中，凡是实数计算都会存在无限的精度跟有限的内存之间的矛盾。
# 在系统底层计算浮点数时使用二进制经过了他的转换，就出现了"误差"
print('======')
# 要想精确计算可以使用Decimal库
from decimal import Decimal
a = Decimal('1')
b = Decimal('0.2')
print('使用decimal计算 1+0.2+0.2+0.2=%s'%(a+b+b+b))
print('正常计算 1+0.2+0.2+0.2=%s'%(1+0.2+0.2+0.2))

print('======')
# lambda表达式的使用
def addNum(x,y):
    return( x+ y )
addNum(3,5)
# 上面的函数改成lambda如下：
lambda x, y: x+y


print('============================================================')
# 经常使用的内置函数
# 做合并或者累加工作的时候经常使用到以下几个函数
# filter(),map(),reduce(),zip()

# 在python3中如果在filter中使用lambda, 必须要使用list转换成列表
a = [1, 2, 3, 4, 5]
print('filter的使用：%s' %list(filter(lambda x : x >2 , a)))

# map的作用把多个参数依次进行处理
a = [1, 2, 3]
print('map的使用：%s' %list(map(lambda x: x +1 , a)))
b = [4, 5, 6]
# list(map(lambda x, y: x +y , a, b))
print('map的使用(多个参数)：%s' %list(map(lambda x, y: x +y , a, b)))

# reduce不能直接使用，必须使用functools模块进行导入
from functools import reduce
# reduce(lambda x, y: x+y, [2, 3, 4], 1)
print('reduce的使用：%s' %reduce(lambda x, y: x+y, [2, 3, 4], 1))

# zip的使用
for i in zip([1, 2, 3], [4, 5, 6]):
    print(i)
# 结果为：(1, 4)，(2, 5)，(3, 6)

# zip 可以进行字典的key/valude对调
dicta = {'a':'a_value' , 'b':'b_value'}
dictb = zip(dicta.values(), dicta.keys())
print(dictb) # 结果是 zip object，所以需要转换成dict输出
print(dict(dictb))

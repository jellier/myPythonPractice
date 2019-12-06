# 函数的高级功能：闭包和装饰器
#############################################################################
# 利用闭包实现累加的写法
# 函数的写法
import time


def func():
    a = 1
    b = 2
    return a + b

# 闭包的写法
# 外部函数中的变量被内部函数引用就叫闭包
# 返回的add 是函数名，单独使用add是函数名称或者函数引用，如果使用add()叫函数调用


def sum(a):
    def add(b):
        print('a is %s, b is %s' % (a, b))
        return a + b
    return add


num1 = func()
num2 = sum(2)
print(num2(4))
print(type(num1))  # int
print(type(num2))  # function
##########################################################################
# 使用闭包实现计数器
# 套路写法：
# def counter():
#     def add_one():
#
#     return add_one
#
# counter()


def counter(_first=0):
    cnt = [_first]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num3 = counter()
num4 = counter(5)
num5 = counter(10)
print('num3第一次累加后为：%s' % num3())
print('num3第二次累加后为：%s' % num3())
print('num3第三次累加后为：%s' % num3())
print('num4第一次累加后为：%s' % num4())
print('num4第二次累加后为：%s' % num4())
print('num4第三次累加后为：%s' % num4())
print('num5第一次累加后为：%s' % num5())
print('num5第一次累加后为：%s' % num5())

#################################################################
# 实现 a * x + b = y 的功能
# 当a和b不变，只需要传入x 即可得到y

# def a_line(a , b):
#     def arg_y(x):
#         return  a * x +b
#     return arg_y

# 上面的代码换成lambda实现


def a_line(a, b):
    return lambda x: a * x + b


# a = 3 ,b = 5
# x = 10 , y=?
line1 = a_line(3, 5)
print(line1(10))
print(line1(20))
line2 = a_line(5, 10)
print(line2(10))
print(line2(20))
print('=======================================')
#################################################################
# 装饰器的使用
# 引用time库
# print(time.time())

# def i_can_sleep():
#     time.sleep(3)
#
# start_time = time.time()
# i_can_sleep()
# end_time = time.time()
# print('运行了%s秒'%(end_time-start_time))
#
#


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('运行了%s秒' % (end_time - start_time))
    return wrapper

# timer是i_can_sleep的装饰器
@timer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()

################################################################
# 带参数的装饰器的写法：

# def tips(func):
#     def nei(a,b):
#         print('start')
#         func(a,b)
#         print('end')
#     return nei
#
# @tips
# def add_func(a , b):
#     print(a + b)
#
# @tips
# def sub_func(a, b):
#     print(a - b)
#
# print(add_func(4,6))


def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('end')
        return nei
    return tips


@new_tips('add_tip')
def add_func(a, b):
    print(a + b)


@new_tips('sub_tip')
def sub_func(a, b):
    print(a - b)


print(add_func(4, 6))

print(sub_func(4, 6))

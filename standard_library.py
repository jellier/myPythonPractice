# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__


# re可以进行匹配和搜索，详见RETest.py
# 以下需要重点掌握
# . ^ $ * + ? {m} {m,n} [] |  \d \D \s ()  常用的元字符
# ^$  空行，什么文本都没有
# .*? 不使用贪婪模式

from pathlib import Path
import os
import random
import datetime
import time
import re
print('=============reR================')
# p = re.compile('..')
p = re.compile('.{3}')
print(p.match('abc'))

# r代表原样输出，不要进行转义，比如不要去掉\n print(r'\nx\n')
# print(r'\nx\n')

# ()代表分组，和group配合使用
# p2 = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
p2 = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
print('不分组：', p2.match('2019-5-20'))
print('group分组：', p2.match('2019-5-20').group())
print('group分组取其中一组：', p2.match('2019-5-20').group(1))
print('groups分组可以取全部分组：', p2.match('2019-5-20').groups())


# match()函数 与 search()函数基本是一样的功能，
# 不一样的就是match()匹配字符串开始位置的一个符合规则的字符串，search()是在字符串全局匹配第一个合规则的字符串
print('match:', p2.match('aa2019-5-20bb'))
print('search:', p2.search('aa2019-5-20bb'))

# sub函数是re模块中非常有用的方法，主要功能是替换原字符串中的部分字符
# 把"#这是我的电话号码去掉"
# sub有三个参数，第一个是匹配规则，第二个是要替换成的字符串/格式，第三个是需要被修改的字符串
phone = '135-0004-9999 #这是我的电话号码'
p3 = re.sub(r'#.*$', '', phone)
print(p3)
# 把上面的电话号码中的-去掉
p4 = re.sub(r'-', '', p3)
print(p4)




# time和datetime模块
# time用于日期和时间的查看，datetime用于日期和时间的修改，比如获得十分钟后的时间

print('=============time================')
print(time.time())
print('localtime：', time.localtime())  # 返回一个time.struct_time时间元组
print('localtime.tm_year：', time.localtime().tm_year)
print(
    'asctime 本地时间为：',
    time.asctime(
        time.localtime(
            time.time())))  # asctime()是最简单的获取可读的时间模式的函数
print('strftime：', time.strftime('%Y-%m-%d %H:%M:%S'))  # strftime 方法可以用来格式化日期
print('strftime：', time.strftime('%Y%m%d'))

print('=============datetime================')
nowtime = datetime.datetime.now()
print('当前时间是：', nowtime)
# 获得10分钟后的时间
newtime = datetime.timedelta(minutes=10)
print('10 分钟后是：', nowtime + newtime)

# 求某天后10天是哪一天
one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print('oneday 10天后是：', one_day + new_date)


# 数学相关的库：math和random
# 数学相关库主要用在机器学习和深度学习中
# 比如math中的sin 和 cos的计算
# random经常用于软件测试
print('=============math================')
print('random随机取整数', random.randint(1, 5))
print('random随机取字符串', random.choice(['aa', 'bb', 'cc']))


print('=============file================')
# os.path 和 pathlib
# pathlib: https://docs.python.org/3/library/pathlib.html
print('当前路径：', os.path.abspath('.'))   # 根据相对路径获取绝对路径
print('上一级路径：', os.path.abspath('..'))
print('Users目录是否存在：', os.path.exists('/Users'))
print('Users目录是否是目录：', os.path.isdir('/Users'))
# os.path.join('tmp/a','b/c')   连接路径


p = Path('.')
print(p.resolve())  # 相当于os.path.abspath

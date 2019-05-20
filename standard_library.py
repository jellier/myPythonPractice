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

import re
# p = re.compile('..')
p = re.compile('.{3}')
print(p.match('abc'))

# r代表原样输出，不要进行转义，比如不要去掉\n print(r'\nx\n')
# p2 = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')

# ()代表分组，和group配合使用
p2 = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
print('不分组：', p2.match('2019-5-20'))
print('group分组：', p2.match('2019-5-20').group())
print('group分组取其中一组：', p2.match('2019-5-20').group(1))
print('groups分组可以取全部分组：', p2.match('2019-5-20').groups())

# print(r'\nx\n')


# match()函数 与 search()函数基本是一样的功能，
# 不一样的就是match()匹配字符串开始位置的一个符合规则的字符串，search()是在字符串全局匹配第一个合规则的字符串
print('match:', p2.match('aa2019-5-20bb'))
print('search:', p2.search('aa2019-5-20bb'))

phone = '135-0004-9999 #这是我的电话号码'
# 把"#这是我的电话号码去掉"
# sub有三个参数，第一个是匹配规则，第二个是要替换成的字符串/格式，第三个是需要被修改的字符串
p3 = re.sub(r'#.*$','',phone)
print(p3)
# 把上面的电话号码中的-去掉
p4 = re.sub(r'-','',p3)
print(p4)
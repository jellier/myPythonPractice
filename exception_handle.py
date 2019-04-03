# NameError
# i=j


# IndexError
# a='123'
# print(a[3])

# 如果输入的是字符，会报ValueError
# year = int(input('请输入年份'))

try:
    year = int(input('请输入年份'))
except ValueError:
    print('年份需要输入数字')

# Exception 可以是多种异常，写成元组的形式即可
# except (valueError, IndexError,KeyError)


# 可以把错误信息打印出来
try:
    print(1/0)
except Exception as e:
    print("%s"%e)

# 自定义错误信息，使用raise
try:
    raise NameError('helloErr')
except NameError:
    print('my customer Err')
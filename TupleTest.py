# 元组：Tuple
# 元组被称为只读列表，数据可被查询，但不能被修改，类似于列表的切片操作，元组写在小括号里面（）元素之前用逗号隔开
# 对于一些不想被修改的数据，可以用元组来保存

# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

# 创建元组
tup1 = ()
# 元组中只有一个元素时，需要在后面添加,
tup1 = (1, )

# 访问元组：
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合。

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)   # 返回：(12, 34.56, 'abc', 'xyz')

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。
del tup3
# print(tup3)  删除后打印会报错


# 元组运算符
print(len((1,2,3))) # 计算元素个数
print((1,2,3)+ (4, 5,6)) # 连接
print(('hello world', )*4)  # 复制
print(3 in (1, 3 ,6)) #判断是否存在
print('返回元组元素的个数：', (1, 3 ,6 , 3).count(3)) # 返回个数
print(max(1, 2, 3))
print(min(1, 2, 3))
testTup = [1,2,3]
print(type(testTup))
print(type(tuple(testTup))) #使用tuple将list转化为元组
# 迭代
# for x in (1, 3, 4):
#     print(x)
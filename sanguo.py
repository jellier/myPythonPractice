# 统计三国的人物名称和武器出现次数

# 读取人名
f = open('sanguo_name.txt')
data = f.read().split('|')
print(data)

# 读取兵器的名称
# 使用stip过滤无用的内容
f2 = open('sanguo_weapon.txt')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1

# 读取书的内容
f3 = open('sanguo_book.txt', encoding='gb18030')
# print(f3.read().strip('\n'))
print(f3.read().replace('\n',''))
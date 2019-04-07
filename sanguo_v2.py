# 统计三国人物和兵器出现次数
# with open的使用？
# re库的用法？


import re
# 定义一个函数用来查找某个人名在文件中出现了多少次
def find_item(hero):
    with open('sanguo_book.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        _name_num = len(re.findall(hero, data))
        # print('%s 出现了 %s 次' % (hero, _name_num))
    return _name_num

# 建立一个字典存储人物名字（key）和出现次数(value)
name_dict={}
with open('sanguo_name.txt') as f:
    names = f.read().split('|')
    # print(names)
    for n in names:
        name_num = find_item(n)

        name_dict[n] = name_num


# 统计武器出现次数

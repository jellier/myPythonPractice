# 统计三国人物和兵器出现次数
# with open的使用？
# re库的使用：正则表达式库

import re
# 定义一个函数用来查找某个人名在文件中出现了多少次
def find_name(hero):
    with open('sanguo_book.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        _name_num = len(re.findall(hero, data))
        # print('%s 出现了 %s 次' % (hero, _name_num))
    return _name_num


# 定义函数查找某个武器出现在文件中多少次
def find_weapon(tool):
    with open('sanguo_book.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        _weapon_num = len(re.findall(tool, data))
        # print('%s 出现了 %s 次' % (tool, _weapon_num))
    return _weapon_num


# 将find_name与find_weapon合并成一个函数
def find_item(_item):

    with open('sanguo_book.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        _num = len(re.findall(_item, data))
        # print('%s 出现了 %s 次' % (tool, _item))
    return _num


# 建立一个字典存储人物名字（key）和出现次数(value)
name_dict={}
with open('sanguo_name.txt') as f:
    names = f.read().split('|')
    for n in names:
        # name_num = find_name(n)
        name_num = find_item(n)
        name_dict[n] = name_num
    print(name_dict)


# 统计武器出现次数，同样定义一个字典，名称为key，次数为value
weapon_dict = {}
with open('sanguo_weapon.txt') as f:
    # 把回车用|替换，因为每隔一行有一行空行，所以替换后兵器之间会有两个|，需要再一次过滤
    weapons = f.read().replace('\n', '|').split('||')
    # print(weapons)
    for w in weapons:
        # weapon_num = find_weapon(w)
        weapon_num = find_item(w)
        weapon_dict[w] = weapon_num
    print(weapon_dict)



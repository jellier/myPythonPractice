#字典推导式的使用
# 数组
alist=[]
for i in range(1, 11):
    if i% 2 == 0:
        alist.append(i*i)
print(alist)
print('==========')
blist = [i*i for i in range(1, 11) if i % 2 == 0]
print(blist)
if alist == blist:
    print('bingo')

print('==========')
# 字典
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zNum = { i: 0 for i in chinese_zodiac}
print(zNum)
print(zNum.keys())
print(zNum.values())

print('==============================================')
# 查字典小游戏
# 当输入 a 往字典里添加条目，输入 l 查找条目，输入 q 退出游戏
def dictionaryFunc():
    dict={}
    userCommand = input("Add or Look up a word(a/l)?")
    while userCommand != 'q':
        # print('Now the dictionary is %s' %dict)
        if userCommand == 'a' :
            # print('add word')
            addWord = input('Type the word: ')
            addDef = input("Type the definition:")
            dict[addWord] = addDef

        elif userCommand == 'l' :
            # print('look up')
            lookWord =  input('Type the word: ')
            if lookWord in dict.keys():
                print(dict[lookWord])
            else:
                print("The word isn't in this dictionary")

        userCommand = input("Add or Look up a word(a/l)?")


dictionaryFunc()




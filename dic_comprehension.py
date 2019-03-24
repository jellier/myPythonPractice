#字典推导式的使用
# 数组
alist=[]
for i in range(1, 11):
    if i% 2 == 0:
        alist.append(i*i)
print(alist)

blist = [i*i for i in range(1, 11) if i % 2 == 0]
print(blist)
if alist == blist:
    print('bingo')

# 字典
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zNum = { i: 0 for i in chinese_zodiac}
print(zNum)
print(zNum.keys())
print(zNum.values())



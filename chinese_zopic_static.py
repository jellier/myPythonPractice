# 统计星座和生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23),
               (9, 23), (10, 23), (11, 23), (12, 23))


# json格式{'x':1,'y':2}在python里面叫字典
# 声明两个字典，用于存储每个星座和生肖的个数
# 初始化，所有生肖和星座数都为0

# cz_num = {}
# for i in chinese_zodiac:
#     cz_num[i] = 0
#
# z_num = {}
# for i in zodiac_name:
#     z_num[i] = 0

#  用"字典推导式"来代替上面的循环
cz_num = {i: 0 for i in chinese_zodiac}
z_num = {i: 0 for i in zodiac_name}
# print(cz_num)
# print(z_num)

# 赋值后cz_num = {'猴': 0, '鸡': 0, '狗': 0, '猪': 0, '鼠': 0, '牛': 0, '虎': 0, '兔': 0, '龙': 0, '蛇': 0, '马': 0, '羊': 0}
# 赋值后z_num = {'摩羯座': 0, '水瓶座': 0, '双鱼座': 0, '白羊座': 0, '金牛座': 0, '双子座': 0, '巨蟹座': 0, '狮子座': 0,
# '处女座': 0, '天秤座': 0, '天蝎座': 0, '射手座': 0}


while True:

    int_year = int(input('请输入出生年份：'))
    int_month = int(input('请输入出生月份：'))
    int_day = int(input('请输入出生日期：'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day <= 23:
            break
        n += 1
    print('您的星座是:' + zodiac_name[n])
    print('%s年的生肖是:%s' % (int_year, chinese_zodiac[int_year % 12]))

    # 给字典赋值
    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    # 输出统计信息
    for key in cz_num.keys():
        if cz_num[key] != 0:
            print('生肖%s的个数是:%d' % (key, cz_num[key]))
    for key in z_num.keys():
        if z_num[key] != 0:
            print('星座%s的个数是:%d' % (key, z_num[key]))


# 根据输入的月份和日期判断星座
# if 和 while的使用
# 序列中的元组，u代表unicode
# if后不需要小括号


zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23),
               (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input('请输入出生月份：'))
int_day = int(input('请输入出生日期：'))

# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#
#         print('您的星座是：' + zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print('您的星座是：' + zodiac_name[0])
#         break


# while 循环方式
n= 0
while zodiac_days[n] < (int_month, int_day):
    if int_month == 12 and int_day <= 23:
        break
    n += 1
print('您的星座是:' + zodiac_name[n])


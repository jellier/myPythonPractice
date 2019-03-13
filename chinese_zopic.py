# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
print(chinese_zodiac[-1])

# 序列中的元组，u代表unicode

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
               u'处女座', u'天秤座', u'天蝎座', u'射手座')
for year in range(2000, 2020):
    print('%s 是%s年' %( year , chinese_zodiac[year%12]))

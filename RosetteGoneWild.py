import turtle
t = turtle.Pen()
num = int(turtle.numinput("input","How many sides do you want to make flower?",6))
turnLeft = 360/num
for x in range(num):
    t.circle(40)
    t.left(turnLeft)
    #添加以下3行代码使花增加内层花蕊
    for y in range(4):
        t.circle(20)
        t.left(90)

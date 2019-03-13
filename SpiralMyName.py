import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colorArr=["red","blue","yellow","green"]
#get input in turtle's Window
yourName = turtle.textinput("Input your name","What's your name?")
# print in loop
for x in range(100):
    t.pencolor(colorArr[x%4])
    #penup is for moving without mark
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(yourName)
    t.left(92)

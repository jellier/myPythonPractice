#random.randint(min,max)
#random.choice(Arrname)
#random.randrange(min,max)

#turtle.window_width(),turtle.window_height()

import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black");
penColors = ["red","blue","green","yellow","pink","brown"]
half_window_width = turtle.window_width()//2
half_window_height = turtle.window_height()//2
size = 0
for i in range(10):
    #print(i)
    t.pencolor(random.choice(penColors))
    size = random.randint(10,60)
    x= random.randrange(-half_window_width,half_window_width)
    y= random.randrange(-half_window_height,half_window_height)
    
    t.penup()
    t.setpos(x,y)
    t.pendown()
# draw the spiral in random size
    for m in range(size):
        t.forward(size)
        t.left(61)
    

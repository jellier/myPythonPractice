import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors=["red","blue","green","yellow","white","pink","brown","gray"]
sides = int(turtle.numinput("Sides input","How many sides do you want?",4,1,8))
turnLeft = 360/sides+2
for x in range(100):
    t.pencolor(colors[x%sides])
    t.circle(x)
    t.left(turnLeft)


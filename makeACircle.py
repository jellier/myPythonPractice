import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors=["red","blue","green","yellow"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(92)


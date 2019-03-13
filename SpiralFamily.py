import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors=["yellow","red","green","blue","orange","white","pink","brown"]
name = turtle.textinput("input","Enter a name or hit [Enter] to quit: ")
myFamily = []
while name!= "" :
    myFamily.append(name)
    #下面这句容易漏掉
    name = turtle.textinput("input","Enter a name or hit [Enter] to quit: ")

#Draw the spiral
for x in range(40):
    lenFamily=  len(myFamily)
    t.pencolor(colors[x%lenFamily])
    t.penup()
    t.forward(x*5)
    t.pendown()
    
    #t.write(myFamily[x%lenFamily])--字体等大，螺旋效果需要把字体逐渐变大
    t.write(myFamily[x%lenFamily],font=("Arial",int((x+20)/4),'bold'))
    #t.left(360/lenFamily)
    t.left(360/lenFamily+2)
    
    
    

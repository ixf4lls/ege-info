import turtle
t=turtle.Turtle()
t.reset()
t.seth(90)
t.width(2)
t.speed(20)
k = 10 #коэффициент для увеличения масштаба
t.right(180)
t.forward(5*k)
t.right(90)
t.forward(50*k)
t.right(90)
t.forward(5*k)
for i in range(5):
    t.seth(90)
    t.circle(-5*k,180)
t.penup()   
for x in range(0,-14,-1):
    for y in range(-5,8):
        t.goto(x*k , y*k ) 
        t.dot(5)
turtle.mainloop()
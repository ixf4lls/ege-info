from turtle import *
tracer(0)
m = 50
screensize(2000, 2000)

for i in range(4):
    for j in range(4):
        forward(m*6)
        right(90)
    forward(m*10)
    right(90)
    forward(3)
penup()

for x in range (-30, 30):
    for y in range (-30, 30):
        setpos(x*m,y*m)
        dot(5, 'red')

done()
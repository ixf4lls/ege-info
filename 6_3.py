from turtle import *
tracer(0)
m = 10
screensize(2000, 2000)

for i in range(4):
    forward(m*7)
    right(90)
    forward(m*7)
    left(90)
    forward(m*7)
    right(90)

penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*m, y*m)
        dot(1, 'red')

done()
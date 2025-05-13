from turtle import *
tracer(0)
m = 10
screensize(2000*2000)

# Повтори 9 [Вперёд 22 Направо 90 Вперёд 6 Направо 90]
# Поднять хвост
# Вперёд 1 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90] 

for i in range (1, 10):
    forward(m*22)
    right(90)
    forward(m*6)
    right(90)

penup()
forward(m*1)
right(90)
forward(m*5)
left(90)
pendown()

for i in range(1, 10):
    forward(m*53)
    right(90)
    forward(m*75)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(m*x, m*y)
        dot(2, 'red')

done()
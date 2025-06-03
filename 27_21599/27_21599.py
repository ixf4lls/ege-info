from math import dist

f = open('27_21599/27_A_21599.txt')

data = []
for line in f:
    line = line.replace(',', '.')
    data.append([float(x) for x in line.split()])

clusters = [[], [], []]

for x, y in data:
    if y < -5:
        clusters[0].append([x, y])
    elif y > x - 10:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

from turtle import *
from random import *
tracer(0)
screensize(10000, 10000)
up()

for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x*10, y*10)
        dot(5, color)

update()
done()

from math import dist

f = open('27_21932/27_B_21932.txt')

data = []
for line in f:
    line = line.replace(',', '.')
    data.append([float(x) for x in line.split()])


def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1]
    if cluster:
        for p in cluster: data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster


clusters = []
while data:
    clusters.append(get_cluster(data[0]))


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


def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]


min_cluster = min(clusters, key=len)
max_cluster = max(clusters, key=len)

print(int(centroid(min_cluster)[0] * 10000), int(centroid(max_cluster)[1] * 10000))
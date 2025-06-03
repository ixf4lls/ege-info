from math import dist

f = open('27/demo_2025_27_Б.txt')

data = []
for line in f:
    line = line.replace(',', '.')
    data.append([float(x) for x in line.split()])


def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if cluster:
        for p in cluster: data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, []) 
    return cluster


clusters = []
while data:
    cluster = get_cluster(data[0])
    clusters.append(cluster)

from turtle import *
from random import *
tracer(0)
up()
screensize(10000, 10000)
for cluster in clusters:
    color = random(), random(), random()
    for x, y in cluster:
        goto(x * 50, y * 50)
        dot(5, color)
update()
done()

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]


centroids = [centroid(cluster) for cluster in clusters]

Px = int(sum(x for x, y in centroids) / len(centroids) * 10000)
Py = int(sum(y for x, y in centroids) / len(centroids) * 10000)

print(Px, Py)
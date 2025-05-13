from itertools import *

cnt = 0
total = 0

for i in product(sorted('АЛГОРИТМ'), repeat=5):
    cnt += 1
    if i[0] != 'Г' and cnt%2 ==1 and i.count('И') >=2:
        total += 1
print(total)
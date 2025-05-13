from itertools import *

cnt = 1
for i in product(sorted('БКФЦ'), repeat=5):
    if cnt == 239:
        print(cnt, i)
    cnt += 1
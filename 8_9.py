from itertools import *

cnt = 1
for w in product(sorted('СЛОН'), repeat=4):
    if cnt == 250:
        print(w)
    cnt +=1 
from itertools import *

cnt = 0

for w in product(sorted('ВИШНЯ'), repeat=6):
    if w.count('В')>1 or w[0]=='Ш' or w[5]=='И' or w[5]=='Я':
        continue
    cnt += 1

print(cnt)
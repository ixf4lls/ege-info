from itertools import *

cnt = 0
for i in product(sorted('ВИНТ'), repeat=5):
    a = ''.join(i)
    cnt += 1
    print(cnt, a)
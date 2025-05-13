from itertools import *

cnt = 0

s = set()

for w in product(sorted('ПРАВО'), repeat=5):
    word = ''.join(w)
    if word.count('П') != 1:
        continue
    if word not in s:
        s.add(word)
        cnt +=1
print(cnt)
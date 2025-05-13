from itertools import *

cnt = 0

for w in product(sorted('КОНФЕТА'), repeat=5):
    word = ''.join(w)
    if word.count('Е') != 2 or word[1] == 'Ф':
        continue
    cnt += 1

print(cnt)
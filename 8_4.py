from itertools import *

cnt = 0

for i in permutations('ПОЛИНА', 6):
    word = ''.join(i)
    word = word.replace('Л', 'П').replace('Н', 'П').replace('И', 'О').replace('А','О')
    if 'ПП' not in word and 'ОО' not in word:
        cnt += 1
print(cnt)
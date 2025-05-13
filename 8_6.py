from itertools import *

cnt = 0

for w in permutations('ПОЛИНА'):
    word = ''.join(w)
    word = word.replace('И', 'О').replace('А', 'О').replace('Л', 'П').replace('Н', 'П')
    if 'ОО' not in word and 'ПП' not in word:
        cnt += 1
print(cnt)
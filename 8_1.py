from itertools import *
s = set()

for i in permutations('МАРИНА', 6):
    a = ''.join(i)
    if a[0] not in 'АИ':
        s.add(a)
print(len(s))
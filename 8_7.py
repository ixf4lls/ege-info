from itertools import *

cnt = 0

for n in product('012345678', repeat=11):
    sum = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) + int(n[4]) + int(n[5]) + int(n[6]) + int(n[7]) + int(n[8])
    if (sum%2 == 0 and n[1] > n[0]) or (sum%2 == 1 and n[1] < n[0]):
        cnt += 1
    print(n)
print(cnt) 
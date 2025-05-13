from collections import Counter

f = open('9_6/input.txt')

cnt = 0

for line in f:
    a = [int(x) for x in line.split()]
    m = max(a)
    sumOth = sum(a) - m
    twoSum = True if a[0]+a[1]==a[2]+a[3] or a[0]+a[2]==a[1]+a[3] or a[0]+a[3]==a[1]+a[2] else False
    if m < sumOth and twoSum:
        cnt += 1

print(cnt)
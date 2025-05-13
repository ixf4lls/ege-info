from collections import Counter

f = open('9_5/input.txt')
cnt = 0

for line in f:
    a = [int(x) for x in line.split()]
    counter = Counter(a)

    m = max(a)
    r = []

    for c, count in counter.items():
        if count > 1:
            r.extend([c] * count)
    
    if m not in r and len(r) > 0 and sum(r) < m:
        cnt += 1

print(cnt)
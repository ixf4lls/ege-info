from collections import Counter

f = open('9_1/input.txt')
cnt = 0

for line in f:
    a = [int(x) for x in line.split()]

    counter = Counter(a)

    a1 = []
    a3 = []
    r = []

    for c, count in counter.items():
        if count >= 3:
            a3.append(c)
        if count == 1:
            a1.append(c)
        if count > 1:
            r.append(c)
    
    a1Avg = sum(a1) / len(a1) if len(a1) > 0 else 0
    rAvg = sum(r) / len(r) if len(r) > 0 else 0

    if rAvg > a1Avg and len(a3) > 0 and len(a1) > 0:
        cnt += 1

print(cnt)
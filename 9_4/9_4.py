from collections import Counter

f = open('9_4/input.txt')
cnt = 0

for line in f:
    a = [int(x) for x in line.split()]

    counter = Counter(a)

    a3 = []
    r = []
    u = []

    for c, count in counter.items():
        if count == 3:
           a3.append(c)
        if count > 1:
            r.append(c)
        if count == 1:
            u.append(c)

        avg = sum(u) / len(u) if len(u) > 0 else 0

        if len(a3) == 1 and len(u) == 4 and avg <= r[0]:
            cnt += 1

print(cnt)
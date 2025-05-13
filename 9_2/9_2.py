from collections import Counter

f = open('9_2/input.txt')
cnt = 0

for line in f:
    a = [int(x) for x in line.split()]

    counter = Counter(a)

    oneEntry = []
    repeats = []

    for c, count in counter.items():
        if count == 1:
            oneEntry.append(c)
        else:
            repeats.extend([c] * count)
    
    repeatsAvg = sum(repeats) / len(repeats) if len(repeats) > 0 else 0
    othersAvg = sum(oneEntry) / len(oneEntry) if len(oneEntry) > 0 else 0

    if len(repeats) == 2 and len(oneEntry) == 4 and repeatsAvg < othersAvg:
        cnt += 1

print(cnt)
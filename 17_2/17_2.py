a = [int(x) for x in open('17_2/1.txt')]

cnt = 0
sums = []

for x in range(len(a) - 1):
    for y in range(x+ 1, len(a) - 1):
        s = a[x] + a[y]
        if s%80 == 0 and (a[x]%50 == 0 or a[y]%50 == 0):
            cnt += 1
            sums.append(s)

print(cnt, max(sums))
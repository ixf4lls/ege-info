a = [int(x) for x in open('17_3/1.txt')]

cnt = 0
sums = []

mn = min(x for x in a if abs(x)%10 == 7)

for i in range(len(a) - 1):
    s = a[i]**2 + a[i+1]**2
    if ((abs(a[i])%10==7) != (abs(a[i+1])%10==7)) and s < mn**2:
        cnt += 1
        sums.append(s)

print(cnt, max(sums))
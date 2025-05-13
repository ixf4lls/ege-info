a = [int(x) for x in open('17_1/1.txt')]

cnt = 0
sums = []

max321 = max(x for x in a if abs(x) >= 100 and str(x)[-1]=='1' and str(x)[-2]=='2' and str(x)[-3]=='3')

for i in range(len(a) - 3):
    num5 = 0
    if 10000<=abs(a[i])<=99999: num5 += 1
    if 10000<=abs(a[i+1])<=99999: num5 += 1
    if 10000<=abs(a[i+2])<=99999: num5 += 1

    s = a[i]+a[i+1]+a[i+2]
    if num5 == 2 and (a[i]%5==0 or a[i+1]%5==0 or a[i+2]%5==0) and (s>max321):
        cnt += 1
        sums.append(s)

print(cnt, max(sums))
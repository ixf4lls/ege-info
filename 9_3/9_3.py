f = open('9_3/input.txt')

cnt = 0

for line in f:
    a = [int(x) for x in line.split()]
    mx = max(a)
    mn = min(a)
    md = sum(a) - mx -mn
    if mx**2 == mn**2 + md**2:
        cnt += 1
        
print(cnt)
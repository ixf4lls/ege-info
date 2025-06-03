f = {}

for n in range(22000):
    if n < 6:
        f[n] = n
    else:
        f[n] = (3 * n - 2)*f[n-5]

print((f[20568] - 51702 * f[20563]) / f[20553])
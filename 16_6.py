f = {}

for n in range(10, 48000):
    if n < 20:
        f[n] = n
    else:
        f[n] = (n-6) * f[n-7]

print((f[47872] - 290*f[47865])/f[47858])
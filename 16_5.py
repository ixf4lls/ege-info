f = {}

for n in range(2100, 50, -1):
    if n >= 2025:
        f[n] = n
    else:
        f[n] = n * 2 + f[n+2]

print(f[82] - f[81])
    
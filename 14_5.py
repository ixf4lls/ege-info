def c(x):
    s = ''
    while x:
        s = str(x % 5) + s
        x //= 5
    return s

max_x = 0

for x in range(2005, 0, -1):
    val = c(4**163 * 5 + 12**62 - x)
    if val.count('1') < val.count('4') and x > max_x:
        max_x = x

print(max_x)
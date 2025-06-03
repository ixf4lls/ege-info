def c(x):
    s = ''
    while x:
        s = str(x % 7) + s
        x //= 7
    return s 

max_zeros = max_x = 0

for x in range(2031, 0, -1):
    val = c(7**170 + 7**100 - x)
    if val.count('0') > max_zeros:
        max_zeros = val.count('0')
        max_x = x

print(max_x)
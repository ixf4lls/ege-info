from string import printable


def c(x):
    s = ''
    while x:
        s = printable[x % 5] + s
        x //= 5
    return s

max_zeros = 0
max_x = 0

for x in range(2006, 1, -1):
    temp = 5**150 + 5**98 - x
    exp = c(temp)
    
    if exp.count('0') > max_zeros:
        max_zeros = exp.count('0')
        max_x = x

print(max_x)
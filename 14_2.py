from string import printable

def c(x):
    s = ''
    while x:
        s = printable[x % 7] + s
        x //= 7
    return s

mx = 0

for x in range(2301):
    s = 7**350 + 7**150 - x
    
    if c(s).count('0') == 200:
        mx = max(mx, x)

print(mx)
from string import printable


def c(x):
    s = ''
    while x: 
        s = printable[x % 12] + s
        x //= 12
    return s


print(c(233214))

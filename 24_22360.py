from re import finditer

s = open('24_22360.txt').readline()

reg = r'[1-9AB][0-9AB]*[06]'

mx = max((x.group() for x in finditer(reg, s)), key=lambda x: int(x, 12))

print(s.find(mx) + len(mx) - 1)
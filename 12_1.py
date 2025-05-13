for i in range(61, 1000):
    s = '1' * i
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
    if s == '2211':
        break
print(i)
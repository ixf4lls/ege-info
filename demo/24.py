f = open('24.txt').readline()

curr_len = max_len = 0

operators = '-*'

for i in range(1, len(f)):
    if f[i] in operators and f[i-1] in operators:
        curr_len = 1
    elif f[i-1] in operators and f[i] == '0':
        if i+1 < len(f) and f[i+1].isdigit():
            curr_len = 1
            i += 1
            continue
        else:
            curr_len += 1
    else:
        curr_len += 1

    max_len = max(max_len, curr_len)
    i += 1

print(max_len)
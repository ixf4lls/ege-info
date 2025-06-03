s = open('24_9753.txt').readline()

max_len = 0
for left in range(len(s)):
    for right in range(left + max_len, len(s)):
        c = s[left:right+1]
        if c.count('Y') <= 150:
            max_len = max(max_len, len(c))
        else:
            break

print(max_len)
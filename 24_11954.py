s = open('24_11954.txt').readline()

left = count_x = 0

min_len = 10**1000

for right in range(len(s)):
    if s[right] == 'X':
        count_x += 1
    elif s[right] == 'Y':
        count_x = 0
        left = right + 1
    
    while count_x >= 500:
        min_len = min(min_len, right - left + 1)
        if s[left] == 'X':
            count_x -= 1
        left += 1

print(min_len)

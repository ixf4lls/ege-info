from itertools import * 

cnt = 0

for number in product('0123456789AB', repeat=5):
    if number[0] == '0': continue
    if number.count('7') == 1 and (number.count('9') + number.count('A') + number.count('B')) <= 3:
        cnt += 1

print(cnt)
st = 3 * 3125**8 + 2 *625**7 - 4 *625**6 + 3 *125**5 - 2 *25*4 - 2025 

newStr = []

while st != 0:
    num = st % 25
    newStr.append(str(num))
    st //= 25

print(newStr)
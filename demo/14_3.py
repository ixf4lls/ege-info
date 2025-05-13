init_val = 7**170 + 7**100

for x in range(1, 2031):
    val = init_val - x
    zeros = 0

    while val != 0:
        num = val % 7
        if num == 0:
            zeros += 1
        val //= 7

    if zeros == 71:
        print(x)
f = open('9.txt')

cnt = 0

for line in f:
    a = [int(x) for x in line.split()]
    
    repeats_3 = 0
    unique = 0

    sumRepeats = 0
    sumUnique = 0

    for x in a:
        joins = a.count(x)

        if joins == 1:
            unique += 1
            sumUnique += x

        if joins > 1:
            if joins == 3:
                repeats_3 += 1
            sumRepeats += x

    if repeats_3 == 3 and unique == 3 and sumRepeats**2 > sumUnique**2:
        cnt +=1

print(cnt)

# – в строке только одно число повторяется трижды, остальные числа
# различны;
# – квадрат суммы всех повторяющихся чисел строки больше квадрата
# суммы всех её неповторяющихся чисел    
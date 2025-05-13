for n in range(1, 13):
    bn = bin(n)[2:]
    if n % 2 == 0:
        bn = '10' + bn
    else: 
        bn = '1' + bn + '01'
    result = int(bn, 2)
    print(result)
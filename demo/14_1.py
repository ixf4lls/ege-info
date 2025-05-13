for x in '0123456789ABCDEFGHI':
    c = int('98897'+ x + '21', 19) + int('2' + x + '923', 19)
    if c % 18 == 0:
        print(c//18)

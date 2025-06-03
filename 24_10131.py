s = open('24_10131.txt').readline()

# Словарь вида { префиксная_сумма: индекс_первого_вхождения }
prefixes = {}

balance = 0
max_len = 0

for i in range(len(s)):
    balance += {'A': 1, 'B': -1}.get(s[i], 0)

    # От начала до i строка сбалансирована, т.е. кол-во A = кол-во B.
    # Макс.длина подстроки - длина текущей подстроки (текущий индекс + 1)
    if balance == 0:
        max_len = i + 1
    
    # Если такая сумма уже встречалась, то 
    # 1. Получаем длину сбалансированной подстроки:
    #    текущий индекс - индекс первого вхождения такой суммы (prefixes[balance]).
    # 2. Обновляем максимальную длину по необходимости.
    # Иначе: записываем текущий индекс в словарь префиксов по ключу текущего баланса
    if balance in prefixes:
        balanced_string_len = i - prefixes[balance]
        max_len = max(max_len, balanced_string_len)
    else:
        prefixes[balance] = i
    
print(max_len)
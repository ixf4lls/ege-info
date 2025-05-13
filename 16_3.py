from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 11: return 10
    else: return n + f(n-1)

for i in range(1, 2204):
    f(i)

print(f(2204) - f(2202))
# Largest prime factor.


n = 600851475143
if n % 2 == 0:
    last_factor = 2
    n = n // 2
    while n % 2 == 0:
        n = n // 2
else:
    last_factor = 1

factor = 3
max_factor = n ** 0.5
while n > 1 and factor <= max_factor:
    if n % factor == 0:
        n = n // factor
        last_factor = factor
        while n % factor == 0:
            n = n // factor
        max_factor = n ** 0.5
    factor = factor + 2
if n == 1:
    print(last_factor)
else:
    print(n)

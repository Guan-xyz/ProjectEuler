# Sumation of primes


def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
        return True

sums = 2

for i in range(3, 2000000, 2):
    if is_prime(i):
        sums += i
print(sums)

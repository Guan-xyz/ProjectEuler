# 10001st prime


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

count = 1
result = 1
while count < 10001:
    result += 2
    if is_prime(result):
        count += 1
print(result)

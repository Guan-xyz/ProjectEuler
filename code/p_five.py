# Smallest multiple


# 1, 2, 3, 5, 7, 11, 13, 17, 19
# 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20


def gcd(n1, n2):
    remainder = n1 % n2
    if remainder == 0:
        return n2
    return gcd(n2, remainder)

def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)

result = 1
for i in range(2, 20):
    result = lcm(result, i)

print(result)

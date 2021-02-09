# Special Pythagorean triplet


for a in range(1, 333):
    for b in range(a+1, (1000-1-a) // 2):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a, b, c)
            print(a * b * c)


# Self powers


sums = 0
for i in range(1, 1001):
    sums += i ** i
print(str(sums)[-10:])

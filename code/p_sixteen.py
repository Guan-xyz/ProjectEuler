# Power digit sum


digits = 2 ** 1000
sums = 0
for i in str(digits):
    sums += int(i)

print(sums)

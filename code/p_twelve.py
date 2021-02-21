# Highly divisible triangular number


# n(n+1)/2
def factor_nums(n):
    nums = 0
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            nums += 2
    return nums


target = 1

while 1:
    target += 1
    if target % 2 == 0:
        result = factor_nums(target//2) * factor_nums(target+1)
    else:
        result = factor_nums(target) * factor_nums((target+1)//2)

    if result > 500: break

print(target * (target+1) // 2)

# Multiples of 3 and 5.


def p_one(divisor, limit):
    p = (limit-1) // divisor
    return divisor * (p*(p+1)) // 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(p_one(3, 1000) + p_one(5, 1000) - p_one(15, 1000))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Largest palindrome product.


def reverse(n):
    reverse_d = 0
    while n > 0:
        reverse_d = 10 * reverse_d + n % 10
        n = n // 10
    return reverse_d

def is_palindrome(n):
    return n == reverse(n)


largest_palindrome = 0
a = 999
while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11
    while b >= a:
        if a * b <= largest_palindrome:
            break
        if is_palindrome(a*b):
            largest_palindrome = a * b
        b = b - db
    a = a - 1

print(largest_palindrome)

# Even Fibonacci numbers.


limit = 4000000
sums = 0
a = 1
b = 1
c = a + b

while c < limit:
    sums = sums + c
    a = b + c
    b = c + a
    c = a + b
print(sums)

from math import sqrt


def kt(n):
    if n < 4:
        return n > 1
    if n & 1 ^ 1 or n % 3 == 0:
        return False
    x = int(sqrt(n)) + 1
    for i in range(5, x + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


n = int(input())
d, x = 0, 2

while x ** 8 <= n:
    if kt(x):
        d += 1
    x += 1

x = int(sqrt(n))
y = int(sqrt(x))

for i in range(2, y + 1):
    if kt(i):
        for j in range(i + 1, x // i + 1):
            if kt(j):
                d += 1

print (d)

from math import sqrt


def kt(n):
    if n < 2:
        return 0
    x = int(sqrt(n)) + 1
    for i in range(2, x):
        if int(n % i) == 0:
            return 0
    return 1


n = int(input())
a = list(map(int, input().split()))
b = []
x = 0

for i in a:
    if kt(i):
        b.append(i)

b.sort()

for i in a:
    if kt(i):
        print (b[x], end=" ")
        x += 1
    else:
        print (i, end=" ")

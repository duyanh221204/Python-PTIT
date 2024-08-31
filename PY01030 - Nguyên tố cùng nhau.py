from math import gcd

n, k = map(int, input().split())
d = 0
for i in range(10 ** (k - 1), 10 ** k):
    if gcd(i, n) == 1:
        d += 1
        print (i, end=" ")
        if d == 10:
            d = 0
            print ()

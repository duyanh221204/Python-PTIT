from math import gcd
def kt(n):
    if n < 2:
        return False
    if n < 4:
        return True
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True

for T in range(int(input())):
    d = 0
    n = int(input())
    for i in range(1, n):
        if gcd(i, n) == 1:
            d += 1
    print ("YES" if kt(d) else "NO")

from math import gcd, sqrt

def kt(n):
    if n < 4:
        return n > 1
    x = int(sqrt(n))
    for i in range(2, x + 1):
        if n % i == 0:
            return 0
    return 1

for T in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    s = 0
    for i in str(g):
        s += int(i)
    print ("YES" if kt(s) else "NO")

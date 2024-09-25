from math import gcd

for T in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    while len(a) < n:
        b = list(map(int, input().split()))
        for i in b:
            a.append(i)
    d = 0
    for i in a:
        if i == k:
            d = 1
            break
    if d:
        print (d)
    else:
        d = int(1e9)
        for i in range(n - 1):
            g = a[i]
            for j in range(i + 1, n):
                g = gcd(a[j], g)
                if g == k:
                    d = min(j - i + 1, d)
                    break
        print ("-1" if d == int(1e9) else d)

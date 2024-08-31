for T in range(int(input())):
    n, p = map(int, input().split())
    d = 0
    while n >= p:
        d += (n // p)
        n //= p
    print (d)

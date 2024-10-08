for T in range(int(input())):
    n, x, m = map(float, input().split())
    d = 0
    while n < m:
        d += 1
        n += (n * x / 100)
    print (d)

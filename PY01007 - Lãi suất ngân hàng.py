for T in range(int(input())):
    n, k, m = map(float, input().split())
    x, y = m / n, k / 100 + 1
    d = 1
    while x > y:
        d += 1
        x /= y
    print (d)

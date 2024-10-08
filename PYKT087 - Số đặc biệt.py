for T in range(int(input())):
    n, k = map(int, input().split())
    d, x, mod = 0, 1, int(1e9) + 7
    while k:
        if k & 1:
            d = (d + x) % mod
        x = (x * n) % mod
        k >>= 1
    print (d)

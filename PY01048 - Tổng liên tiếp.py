for T in range(int(input())):
    n = int(input())
    d = 0
    x = 2
    k = n << 1
    while x * (x - 1) < k:
        if k % x == 0:
            a = k // x - x + 1 >> 1
            if a >= 1 and x * ((a << 1) + x - 1) >> 1 == n:
                d += 1
            a = k // (k // x) - k // x + 1 >> 1
            if a >= 1 and x * ((a << 1) + x - 1) >> 1 == n:
                d += 1
        x += 1
    print (d)

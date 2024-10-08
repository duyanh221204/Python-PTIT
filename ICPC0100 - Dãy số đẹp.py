for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    for i in range(n - 1):
        m1, m2 = max(a[i], a[i + 1]), min(a[i], a[i + 1])
        while m1 > m2 << 1:
            d += 1
            m2 <<= 1
    print (d)

for T in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    l, r = [0] * (n + 2), [0] * (n + 2)
    l[0] = int(-2e9)
    r[n + 1] = int(2e9)
    for i in range(1, n + 1):
        l[i] = max(a[i], l[i - 1])
    for i in range(n, 0, -1):
        r[i] = min(a[i], r[i + 1])
    d = 0
    for i in range(1, n):
        if l[i - 1] <= a[i] < r[i + 1]:
            d += 1
    if a[n] >= l[n - 1]:
        d += 1
    print (d)

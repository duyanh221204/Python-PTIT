for T in range(int(input())):
    n = int(input())
    a, b = [], []
    for i in range(n):
        x, y = map(float, input().split())
        a.append(x)
        b.append(y)
    d = 0
    f = [0] * (n + 2)
    for i in range(n):
        f[i] = 1
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                f[i] = max(f[j] + 1, f[i])
        d = max(f[i], d)
    print (d)

for T in range(int(input())):
    n = int(input())
    x, y, z = map(int, input().split())
    f = [0] * (n + 2)
    f[1] = x
    for i in range(2, n + 1):
        f[i] = f[i - 1] + x
        if i & 1:
            f[i] = min(f[i >> 1] + x + z, f[(i >> 1) + 1] + z + y, f[i])
        else:
            f[i] = min(f[i >> 1] + z, f[i])
    print (f[n])

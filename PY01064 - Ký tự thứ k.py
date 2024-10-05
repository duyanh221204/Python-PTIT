def tt(n, k):
    x = 1 << (n - 1)
    if k == x:
        return chr(n + 64)
    if k > x:
        return tt(n - 1, k - x)
    return tt(n - 1, k)


for T in range(int(input())):
    n, k = map(int, input().split())
    print (tt(n, k))

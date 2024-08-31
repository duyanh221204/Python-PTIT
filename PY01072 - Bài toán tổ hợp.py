def tt(a, b, n, k, x):
    for i in range(b[x - 1] + 1, n - k + x + 1):
        b[x] = i
        if x == k:
            for j in range(1, k + 1):
                print (a[b[j]], end=" ")
            print ()
        else:
            tt(a, b, n, k, x + 1)

n, k = map(int, input().split())
a = sorted(set(list(map(int, input().split()))))
a = [0] + a
tt(a, [0] * (k + 2), len(a) - 1, k, 1)

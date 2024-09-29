n = int(input())
a = sorted(list(map(int, input().split())))
print (max(a[0] * a[1], a[n - 2] * a[n - 1], a[0] * a[1] * a[n - 1], a[0] * a[n - 2] * a[n - 1], a[n - 3] * a[n - 2] * a[n - 1]))

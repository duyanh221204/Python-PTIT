n, q = map(int, input().split())
a = [0] * (n + 2)

while q:
    x, y = map(int, input().split())
    a[x] += 1
    a[y + 1] -= 1
    q -= 1

for i in range(1, n + 1):
    a[i] += a[i - 1]
    print (a[i] & 1, end=" ")

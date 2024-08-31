n = int(input())
a = list(map(int, input().split()))
d = 0
for i in range(n - 1):
    if a[i] != a[i + 1]:
        d += 1
print (d)

n = int(input())
a = list(map(int, input().split()))
d = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            d += 1

print (d)

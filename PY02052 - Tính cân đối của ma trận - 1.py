n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())

d1, d2 = 0, 0
for i in range(n):
    for j in range(n):
        if j < i:
            d1 += a[i][j]
        if j > i:
            d2 += a[i][j]

print ("YES" if abs(d1 - d2) <= k else "NO")
print (abs(d1 - d2))

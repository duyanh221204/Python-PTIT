n = int(input())
a = list(map(int, input().split()))
d, x = int(2e9), 0

for i in range(n):
    s = 0
    for j in range(n):
        s += abs(a[i] - a[j])
    if s < d:
        d, x = s, a[i]

print (d, x)

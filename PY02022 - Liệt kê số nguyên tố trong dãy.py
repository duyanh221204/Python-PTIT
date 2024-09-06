k = [1] * 1000002
k[0] = k[1] = 0
for i in range(2, 1001):
    if k[i]:
        for j in range(i * i, 1000001, i):
            k[j] = 0

n = int(input())
a = list(map(int, input().split()))
f = [0] * 1000002

for i in a:
    f[i] += 1

for i in a:
    if k[i] and f[i]:
        print (i, f[i])
        f[i] = 0

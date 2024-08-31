k = [1] * 1000002
k[0] = k[1] = 0
a = []
for i in range(2, 1000001):
    if k[i]:
        a.append(i)
        for j in range(i * i, 1000001, i):
            k[j] = 0

n, x = map(int, input().split())
id = 0
for i in range(n + 1):
    print (x, end=" ")
    x += a[id]
    id += 1

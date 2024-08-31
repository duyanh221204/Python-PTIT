k = [1] * 1002
k[0] = k[1] = 0
for i in range(2, 32):
    if k[i]:
        for j in range(i * i, 1001, i):
            k[j] = 0

n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(m):
        print (k[a[i][j]], end=" ")
    print ()

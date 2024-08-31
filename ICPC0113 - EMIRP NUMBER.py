k, f, a, b = [0] * 1000002, [0] * 1000002, [], []

k[0] = k[1] = 1

for i in range(2, 1001):
    if not k[i]:
        for j in range(i * i, 1000001, i):
            k[j] = 1

for i in range(2, 1000001):
    if not k[i]:
        a.append(i)

for i in a:
    x = int(str(i)[::-1])
    if x != i and not k[x] and not f[i] and not f[x]:
        b.append(i)
        b.append(x)
        f[i] = f[x] = 1

#print (*b)

for T in range(int(input())):
    n = int(input())
    for i in range(0, len(b) - 1, 2):
        if b[i] < n and b[i + 1] < n:
            print (b[i], b[i + 1], end=" ")
    print ()

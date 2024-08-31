k = [0] * 1000002
a = []
k[0] = k[1] = 1
for i in range(2, 1000001):
    if not k[i]:
        a.append(i)
        for j in range(i * i, 1000001, i):
            k[j] = 1

for T in range(int(input())):
    n = int(input())
    d = 0
    for i in range(1, len(a)):
        if a[i] + 6 >= n:
            break
        if not k[a[i] + 2] and not k[a[i] + 6]:
            d += 1
        if not k[a[i] + 4] and not k[a[i] + 6]:
            d += 1
    print (d)

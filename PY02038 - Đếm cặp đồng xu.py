n = int(input())
a = []
for i in range(n):
    b = input()
    a.append(b)

d = 0
for i in range(n):
    d1 = 0
    for j in range(n):
        if a[i][j] == "C":
            d1 += 1
    d += (d1 * (d1 - 1) >> 1)
    d1 = 0
    for j in range(n):
        if a[j][i] == "C":
            d1 += 1
    d += (d1 * (d1 - 1) >> 1)

print (d)

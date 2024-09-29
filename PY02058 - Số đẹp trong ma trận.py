n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

d1, d2 = int(-2e9), int(2e9)

for i in range(n):
    for j in range(m):
        d1 = max(a[i][j], d1)
        d2 = min(a[i][j], d2)

x = 0
for i in range(n):
    for j in range(m):
        if d1 - d2 == a[i][j]:
            x = 1
            break

if not x:
    print ("NOT FOUND")
else:
    print (d1 - d2)
    for i in range(n):
        for j in range(m):
            if d1 - d2 == a[i][j]:
                print (f"Vi tri [{i}][{j}]")

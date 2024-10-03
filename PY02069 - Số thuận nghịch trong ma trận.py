def kt(n):
    return len(str(n)) >= 2 and n == int(str(n)[::-1])


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

d = int(-2e9)

for i in range(n):
    for j in range(m):
        if kt(a[i][j]):
            d = max(a[i][j], d)

if d == int(-2e9):
    print ("NOT FOUND")
else:
    print (d)
    for i in range(n):
        for j in range(m):
            if d == a[i][j]:
                print (f"Vi tri [{i}][{j}]")

def tt(s):
    return len(s.split())


n = int(input())
a = []
for i in range(n):
    a.append(input())

d, x, v = 0, 0, []

while x < n:
    if tt(a[x]) & 1 ^ 1:
        v.append(1)
        while x < n and tt(a[x]) & 1 ^ 1:
            x += 1
    else:
        v.append(2)
        x += 4

print (len(v))
for i in v:
    print (i)

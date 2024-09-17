def tt(a, b):
    d = 0
    while a != b and d <= len(b):
        d += 1
        a = a[1:] + a[0]
    if d <= len(b):
        return d
    return -1


n = int(input())
s = []
for i in range(n):
    s.append(input())

d = 2e9
for i in range(n):
    x = 0
    for j in range(n):
        if s[i] != s[j]:
            tmp = tt(s[j], s[i])
            if tmp == -1:
                x = -1
                break
            x += tmp
    if x == -1:
        d = -1
        break
    d = min(x, d)

print (d)

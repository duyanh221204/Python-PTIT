s = input()
k, f = [0] * 100, [0] * 100
a = []
x = 0

while x + 1 < len(s):
    y = int(s[x:x+2])
    if not k[y]:
        a.append(y)
        k[y] = 1
    f[y] += 1
    x += 2

for i in a:
    print (i, f[i])

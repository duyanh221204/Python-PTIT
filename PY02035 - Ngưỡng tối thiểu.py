s = input()
n = int(input())
k, f = [0] * 100, [0] * 100
a = []
d, x = 0, 0

while x + 1 < len(s):
    y = int(s[x:x+2])
    if not k[y]:
        a.append(y)
        k[y] = 1
    f[y] += 1
    x += 2

a.sort()

for i in a:
    if f[i] >= n:
        d = 1
        print (i, f[i])

if not d:
    print ("NOT FOUND")

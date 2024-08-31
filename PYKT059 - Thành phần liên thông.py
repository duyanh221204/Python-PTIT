p = [i for i in range(302)]

def tim(x):
    while x != p[x]:
        x = p[x]
    return x

n, m, x = map(int, input().split())
d = 0

while m:
    a, b = map(int, input().split())
    a, b = tim(a), tim(b)
    if a != b:
        p[b] = a
    m -= 1

x = tim(x)
for i in range(1, n + 1):
    if x != tim(i):
        d = 1
        print (i)

if not d:
    print ("0")

v = []
def tt(n, s, a, b, c):
    if len(s) <= n:
        if a and b and c and a <= b <= c:
            v.append(s)
        if len(s) == n:
            return
    tt(n, s + "A", a + 1, b, c)
    tt(n, s + "B", a, b + 1, c)
    tt(n, s + "C", a, b, c + 1)

n = int(input())
tt(n, "", 0, 0, 0)
v.sort(key=lambda x: (len(x), x))
for i in v:
    print (i)

a = []


def tt(n, s, d2, d3, d5, d7):
    if 4 <= len(s) <= n and d2 and d3 and d5 and d7 and int(s) & 1:
        a.append(int(s))
    if len(s) < n:
        tt(n, s + "2", 1, d3, d5, d7)
        tt(n, s + "3", d2, 1, d5, d7)
        tt(n, s + "5", d2, d3, 1, d7)
        tt(n, s + "7", d2, d3, d5, 1)


tt(int(input()), "", 0, 0, 0, 0)

a.sort()

for i in a:
    print (i)

p = [i for i in range(100002)]


def tim(x):
    while x != p[x]:
        x = p[x]
    return x


def hop(x, y):
    x, y = tim(x), tim(y)
    if x != y:
        p[y] = x


q = int(input())
while q:
    x, y, z = map(int, input().split())
    if z == 1:
        hop(x, y)
    else:
        print (int(tim(x) == tim(y)))
    q -= 1

a, res = [], []


def kt(b):
    for i in range(1, len(b)):
        if b[i] > b[i - 1]:
            return 0
    return 1


def tt(n):
    if not n and kt(a):
        s = "("
        for i in a:
            s += (str(i) + " ")
        s = s[:-1]
        s += ")"
        res.append(s)
        return

    if not n:
        return

    for i in range(n, 0, -1):
        if n >= i:
            a.append(i)
            tt(n - i)
            a.pop()


for T in range(int(input())):
    n = int(input())
    a, res = [], []
    tt(n)
    print (len(res))
    for i in res:
        print (i, end=" ")
    print ()

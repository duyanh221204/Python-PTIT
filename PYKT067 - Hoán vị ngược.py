a, k, v = [], [0] * 12, []


def tt(n):
    for i in range(1, n + 1, 1):
        if not k[i]:
            k[i] = 1
            a.append(i)
            if len(a) == n:
                s = ""
                for j in a:
                    s += str(j)
                v.append(s)
            else:
                tt(n)
            k[i] = 0
            a.pop()


for T in range(int(input())):
    a.clear()
    k = [0] * 12
    v.clear()
    tt(int(input()))
    print (len(v))
    for i in range(len(v) - 1, -1, -1):
        print (v[i], end=" ")
    print ()

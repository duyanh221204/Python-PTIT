def tt1(a, p, q):
    s = 0
    for i in a:
        if ord(i) - 48 == q:
            s = s * 10 + p
        else:
            s = s * 10 + ord(i) - 48
    return s

def tt2(a, p, q):
    s = 0
    for i in a:
        if ord(i) - 48 == p:
            s = s * 10 + q
        else:
            s = s * 10 + ord(i) - 48
    return s

for T in range(int(input())):
    a, b = map(int, input().split())
    inp = input().split()
    if len(inp) == 1:
        x1 = inp[0]
        x2 = input()
    else:
        x1, x2 = inp[0], inp[1]
    if a > b:
        a, b = b, a
    print (tt1(x1, a, b) + tt1(x2, a, b), tt2(x1, a, b) + tt2(x2, a, b))

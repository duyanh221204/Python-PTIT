for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = [0] * 1002
    for i in a:
        k[i] = 1
    d, m1, m2 = 0, min(a), max(a)
    for i in range(m1, m2 + 1):
        if not k[i]:
            d += 1
    print (d)

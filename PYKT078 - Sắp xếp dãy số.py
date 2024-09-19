for T in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ng, pt = [], []
    x, d = max(a), 0
    for i in a:
        if i < 0:
            if not d and x == i:
                d = 1
                ng.append(m)
                ng.append(i)
            else:
                ng.append(i)
        else:
            if not d and x == i:
                d = 1
                pt.append(m)
                pt.append(i)
            else:
                pt.append(i)
    for i in ng:
        print (i, end=" ")
    for i in pt:
        print (i, end=" ")
    print ()

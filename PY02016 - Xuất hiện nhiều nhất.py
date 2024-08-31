for T in range(int(input())):
    n = int(input())
    k = [0] * 1000002
    a = list(map(int, input().split()))
    m = 0
    for i in a:
        k[i] += 1
        m = max(k[i], m)
    if m <= n >> 1:
        print ("NO")
    else:
        for i in range(1, 1000001):
            if k[i] == m:
                print (i)

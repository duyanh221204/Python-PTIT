for T in range(int(input())):
    n = int(input())
    k = [0] * 1002
    m = 0
    while n:
        x = int(input())
        k[x] += 1
        m = max(k[x], m)
        n -= 1
    for i in range(1, 1001):
        if k[i] == m:
            print (i)
            break

for T in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x, y, z, d = 0, 0, 0, 0
    while x < n and y < m and z < k:
        if a[x] == b[y] == c[z]:
            d = 1
            print (a[x], end=" ")
            x += 1
            y += 1
            z += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        else:
            z += 1
    if not d:
        print ("NO")
    else:
        print ()

for T in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(d, n):
        print (a[i], end=" ")
    for i in range(d):
        print (a[i], end=" ")
    print ()

for T in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    d = 0
    for i in range(n):
        if a[i] > b[i]:
            d = 1
            print ("NO")
            break
    if not d:
        print ("YES")

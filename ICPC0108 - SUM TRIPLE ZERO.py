for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    d = 0
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                d += 1
                l += 1
            elif a[i] + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    print (d)

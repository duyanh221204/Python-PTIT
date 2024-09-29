for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    for i in a:
        d ^= i
    print (d)

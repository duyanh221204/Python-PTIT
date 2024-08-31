for T in range(int(input())):
    n = int(input())
    d = 0
    if n & 1:
        for i in range(1, n + 1, 2):
            d += (1 / i)
    else:
        for i in range(2, n + 1, 2):
            d += (1 / i)
    print (f"{d:.6f}")

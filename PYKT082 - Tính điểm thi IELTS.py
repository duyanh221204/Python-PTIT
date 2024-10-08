def tt(n):
    if 3 <= n <= 4:
        return 2.5
    if n <= 6:
        return 3.0
    if n <= 9:
        return 3.5
    if n <= 12:
        return 4.0
    if n <= 15:
        return 4.5
    if n <= 19:
        return 5.0
    if n <= 22:
        return 5.5
    if n <= 26:
        return 6.0
    if n <= 29:
        return 6.5
    if n <= 32:
        return 7.0
    if n <= 34:
        return 7.5
    if n <= 36:
        return 8.0
    if n <= 38:
        return 8.5
    return 9.0


for T in range(int(input())):
    r, l, s, w = map(float, input().split())
    tb = (tt(int(r)) + tt(int(l)) + s + w) / 4
    n = int(tb)
    if tb - n == 0.125 or tb - n == 0.625:
        tb -= 0.125
    elif tb - n == 0.25 or tb - n == 0.75:
        tb += 0.25
    elif tb - n == 0.375 or tb - n == 0.875:
        tb += 0.125
    print (f"{tb:.1f}")

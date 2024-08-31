def nt(n):
    if n < 4:
        return n > 1
    x = 2
    while x * x <= n:
        if n % x == 0:
            return 0
        x += 1
    return 1

def kt(n):
    if not nt(len(n)):
        return 0
    d = 0
    for i in n:
        if nt(int(i)):
            d += 1
    return d > len(n) - d

for T in range(int(input())):
    print ("YES" if kt(input()) else "NO")

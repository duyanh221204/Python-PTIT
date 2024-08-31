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
    if not nt(len(str(n))):
        return 0
    d = 0
    for i in str(n):
        if nt(int(i)):
            d += 1
    return d > len(str(n)) - d

for T in range(int(input())):
    print ("YES" if kt(int(input())) else "NO")

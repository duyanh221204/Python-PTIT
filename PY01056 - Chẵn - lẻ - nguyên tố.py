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
    for i in range(len(n)):
        if int(n[i]) & 1 != i & 1:
            return 0
    s = 0
    for i in n:
        s += int(i)
    return nt(s)

for T in range(int(input())):
    print ("YES" if kt(input()) else "NO")

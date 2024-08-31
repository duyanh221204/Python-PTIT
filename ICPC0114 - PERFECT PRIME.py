from math import sqrt

def ktnt(n):
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    x = 5
    while x * x <= n:
        if n % x == 0 or n % (x + 2) == 0:
            return 0
        x += 6
    return 1

def kt(n):
    s = 0
    x = n
    while x:
        if not ktnt(int(x % 10)):
            return 0
        s += int(x % 10)
        x //= 10
    if not ktnt(s):
        return 0
    if not ktnt(n):
        return 0
    if not ktnt(int(str(n)[::-1])):
        return 0
    return 1

for T in range(int(input())):
    print ("Yes" if kt(int(input())) else "No")

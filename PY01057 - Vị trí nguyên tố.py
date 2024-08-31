def kt(n):
    if n < 4:
        return n > 1
    x = 2
    while x * x <= n:
        if n % x == 0:
            return 0
        x += 1
    return 1

for T in range(int(input())):
    n = input()
    d = 0
    for i in range(len(n)):
        if kt(int(n[i])) != kt(i):
            d = 1
            print ("NO")
            break
    if not d:
        print ("YES")

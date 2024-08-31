for T in range(int(input())):
    s = input()
    n = input()
    d, x = 0, s.find(n)
    while x > -1:
        d += 1
        x = s.find(n, len(n) + x)
    print (d)

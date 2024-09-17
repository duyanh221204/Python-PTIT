for T in range(int(input())):
    s = input()
    n = input()
    x, d = s.find(n), 0
    while x != -1:
        d += 1
        x = s.find(n, x + len(n))
    print (d)

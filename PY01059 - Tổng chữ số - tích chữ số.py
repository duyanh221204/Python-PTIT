for T in range(int(input())):
    n = input()
    d, s, h = 0, 1, 0
    for i in range(len(n)):
        if i & 1:
            if int(n[i]):
                h = 1
                s *= int(n[i])
        else:
            d += int(n[i])
    if not h:
        s = 0
    print (d, s)

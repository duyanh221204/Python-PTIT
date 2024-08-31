for T in range(int(input())):
    n = input()
    d, s = 0, 1
    for i in range(len(n)):
        if i & 1 ^ 1:
            if int(n[i]):
                s *= int(n[i])
        else:
            d += int(n[i])
    print (s, d)

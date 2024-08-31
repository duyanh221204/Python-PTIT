for T in range(int(input())):
    s = input()
    c = s[0]
    d = 0
    for i in s:
        if c == i:
            d += 1
        else:
            print (f"{d}{c}", end="")
            c = i
            d = 1
    if d:
        print (f"{d}{c}", end="")
    print ()

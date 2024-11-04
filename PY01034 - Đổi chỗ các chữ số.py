for T in range(int(input())):
    s = list(input())
    x = len(s) - 2
    while x >= 0 and ord(s[x]) <= ord(s[x + 1]):
        x -= 1
    if x < 0:
        print ("-1")
    else:
        y = len(s) - 1
        while y >= 0 and (ord(s[x]) <= ord(s[y]) or (ord(s[y - 1]) == ord(s[y]) and ord(s[y]) < ord(s[x]))):
            y -= 1
        if y < 0:
            print ("-1")
        else:
            s[x], s[y] = s[y], s[x]
            if ord(s[0]) == 48:
                print ("-1")
            else:
                print (''.join(s))

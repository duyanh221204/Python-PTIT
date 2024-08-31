for T in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print (n)
    else:
        d, h = 0, 0
        while True:
            d += 1
            if d == 1001:
                break
            n += int(str(n)[::-1])
            if n % 7 == 0:
                h = 1
                print (n)
                break
        if not h:
            print ("-1")

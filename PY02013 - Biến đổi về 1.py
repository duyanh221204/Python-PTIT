while True:
    n = int(input())
    if not n:
        break
    if n <= 2:
        print (n)
    else:
        d = 1
        while n > 1:
            d += 1
            if n & 1:
                n = n * 3 + 1
            else:
                n >>= 1
        print (d)

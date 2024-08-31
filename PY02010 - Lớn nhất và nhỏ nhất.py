while True:
    n = int(input())
    if not n:
        break
    a = []
    while n:
        x = int(input())
        a.append(x)
        n -= 1
    d1, d2 = min(a), max(a)
    if d1 == d2:
        print ("BANG NHAU")
    else:
        print (d1, d2)

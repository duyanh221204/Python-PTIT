for T in range(int(input())):
    s = input().split()
    d = 0
    for i in s:
        if d + len(i) + 1 <= 100:
            print (i, end=" ")
            d += (len(i) + 1)
        else:
            break
    print ()

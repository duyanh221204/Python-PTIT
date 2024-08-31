for T in range(int(input())):
    s = input()
    d = 0
    a = []
    for i in s:
        if i.isdigit():
            d += int(i)
        else:
            a.append(i)
    a.sort()
    print (''.join(a), end="")
    print (d)

for T in range(int(input())):
    s = input()
    d, k = 0, 0
    m = int(-9e18)
    for i in s:
        if i.isdigit():
            d = 1
            k = k * 10 + ord(i) - 48
        elif d:
            m = max(k, m)
            d, k = 0, 0
    print (max(k, m))

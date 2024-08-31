for T in range(int(input())):
    s = input()
    d, k = 0, 0
    m = int((1 << 63) - 1)
    for i in s:
        if i.isdigit():
            d = 1
            k = k * 10 + ord(i) - 48
        elif d:
            m = min(k, m)
            k = 0
            d = 0
    print (m)

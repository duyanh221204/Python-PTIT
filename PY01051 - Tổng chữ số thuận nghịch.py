for T in range(int(input())):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    print ("YES" if s == int(str(s)[::-1]) and s > 9 else "NO")

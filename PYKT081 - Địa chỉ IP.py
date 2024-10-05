for T in range(int(input())):
    s = input().split(".")
    if len(s) != 4:
        print ("NO")
    else:
        d = 0
        for i in s:
            try:
                m = int(i)
                if m < 0 or m > 255:
                    d = 1
                    break
            except Exception:
                d = 1
                break
        print ("YES" if not d else "NO")

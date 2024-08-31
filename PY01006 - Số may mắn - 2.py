for T in range(int(input())):
    s = input()
    print ("YES" if s.count("4") + s.count("7") == len(s) else "NO")

for T in range(int(input())):
    n = input()
    if len(n) < 3:
        print ("NO")
    else:
        d, x = 0, -1
        for i in range(1, len(n)):
            if int(n[i]) > int(n[i - 1]):
                x = i
            else:
                break
        if x == len(n) - 1:
            print ("NO")
        else:
            for i in range(x + 1, len(n)):
                if int(n[i]) >= int(n[i - 1]):
                    d = 1
                    print ("NO")
                    break
            if not d:
                print ("YES")

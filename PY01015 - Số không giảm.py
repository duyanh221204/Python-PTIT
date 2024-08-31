for T in range(int(input())):
    s = input()
    d = 0
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            d = 1
            print ("NO")
            break
    if not d:
        print ("YES")

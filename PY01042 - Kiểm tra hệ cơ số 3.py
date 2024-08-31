for T in range(int(input())):
    s = input()
    d = 0
    for i in s:
        if i != "0" and i != "1" and i != "2":
            d = 1
            print ("NO")
            break
    if not d:
        print ("YES")

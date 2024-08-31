for T in range(int(input())):
    s = input()
    c = 'A'
    for i in range(len(s)):
        if s[i].isalpha():
            c = s[i]
        else:
            for j in range(int(s[i])):
                print (c, end="")
    print ()

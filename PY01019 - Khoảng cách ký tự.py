for T in range(int(input())):
    s = input()
    k = s[::-1]
    d = 0
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(k[i]) - ord(k[i - 1])):
            d = 1
            print ("NO")
            break
    if not d:
        print ("YES")

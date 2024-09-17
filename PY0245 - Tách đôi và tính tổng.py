s = input()
while len(s) > 1:
    a, b = int(s[:len(s)>>1]), int(s[len(s)>>1:])
    print (a + b)
    s = str(a + b)

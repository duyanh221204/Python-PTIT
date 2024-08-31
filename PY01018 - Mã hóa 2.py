p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    inp = input()
    if inp == "0":
        break
    inp = inp.split()
    k = int(inp[0])
    s = list(inp[1])
    for i in range(len(s)):
        for j in range(28):
            if s[i] == p[j]:
                s[i] = p[(j + k) % 28]
                break
    print (''.join(s)[::-1])

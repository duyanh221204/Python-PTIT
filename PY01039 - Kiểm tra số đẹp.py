def kt(n):
    ss = set()
    for i in n:
        ss.add(i)
    if len(ss) != 2:
        return 0
    for i in range(len(n) - 2):
        if n[i] != n[i + 2]:
            return 0
    return 1

for T in range(int(input())):
    print ("YES" if kt(input()) else "NO")

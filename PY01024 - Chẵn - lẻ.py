def kt(n):
    s = 0
    for i in range(len(n) - 1):
        if abs(int(n[i]) - int(n[i + 1])) != 2:
            return 0
        s += int(n[i])
    s += int(n[-1])
    return int(s % 10) == 0

for T in range(int(input())):
    print ("YES" if kt(input()) else "NO")

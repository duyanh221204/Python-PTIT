def kt(n):
    if len(n) & 1 ^ 1 or len(n) == 1:
        return 0
    if n[0] == n[1]:
        return 0
    for i in range(2, len(n), 2):
        if n[i] != n[i - 2]:
            return 0
    return 1

for T in range(int(input())):
    print ("YES" if kt(input()) else "NO")

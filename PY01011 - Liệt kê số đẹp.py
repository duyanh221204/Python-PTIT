def kt(n):
    if n != n[::-1]:
        return 0
    for i in n:
        if i != "0" and i != "2" and i != "4" and i != "6" and i != "8":
            return 0
    if len(n) & 1:
        return 0
    return 1

a = []
for i in range(22, int(1e6) + 1):
    if kt(str(i)):
        a.append(i)

for T in range(int(input())):
    n = int(input())
    for i in a:
        if i < n:
            print (i, end=" ")
        else:
            break
    print ()

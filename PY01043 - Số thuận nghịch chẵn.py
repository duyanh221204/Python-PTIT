def kt(n):
    if n != int(str(n)[::-1]):
        return 0
    if len(str(n)) & 1:
        return 0
    for i in str(n):
        if int(i) & 1:
            return 0
    return 1

a = []
for i in range(22, 1000001):
    if kt(i):
        a.append(i)

for T in range(int(input())):
    n = int(input())
    for i in a:
        if i < n:
            print (i, end=" ")
        else:
            break
    print ()

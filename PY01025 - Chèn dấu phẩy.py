s = input()
d = 0
k = ""
for i in range(len(s) - 1, -1, -1):
    k += s[i]
    d += 1
    if i > 0 and d % 3 == 0:
        d = 0
        k += ","
print (k[::-1])

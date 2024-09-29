s = input()
k = [0] * 100
x = 0

while x + 1 < len(s):
    y = int(s[x:x+2])
    if not k[y]:
        print (y, end=" ")
        k[y] = 1
    x += 2

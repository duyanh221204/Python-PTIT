f = [0] * 93
f[1] = 1
for i in range(2, 93):
    f[i] = f[i - 2] + f[i - 1]

for T in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print (f[i], end=" ")
    print ()

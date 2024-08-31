k = [0] * 10002
k[0] = k[1] = 1
for i in range(2, 101):
    if not k[i]:
        for j in range(i * i, 10001, i):
            k[j] = 1

for T in range(int(input())):
    print ("YES" if not k[int(input()[-4:])] else "NO")

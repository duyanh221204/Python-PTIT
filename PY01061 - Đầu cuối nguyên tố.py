k = [1] * 1002
for i in range(2, 32):
    if k[i]:
        for j in range(i * i, 1001, i):
            k[j] = 0

for T in range(int(input())):
    n = input()
    print ("YES" if k[int(n[:3])] and k[int(n[-3:])] else "NO")

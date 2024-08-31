gt = [1]
for i in range(1, 10):
    gt.append(gt[i - 1] * i)

for T in range(int(input())):
    s = input()
    d = 0
    for i in s:
        d += gt[int(i)]
    print ("Yes" if d == int(s) else "No")

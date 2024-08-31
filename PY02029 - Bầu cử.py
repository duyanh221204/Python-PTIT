n, m = map(int, input().split())
a = list(map(int, input().split()))
k = [0] * (m + 2)
d1, d2 = int(-2e9), int(-2e9)

for i in a:
    k[i] += 1
    d1 = max(k[i], d1)

for i in a:
    if k[i] < d1:
        d2 = max(k[i], d2)

if d2 == int(-2e9):
    print ("NONE")
else:
    for i in range(1, m + 1):
        if k[i] == d2:
            print (i)
            break

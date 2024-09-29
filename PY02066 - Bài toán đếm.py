n = int(input())
a = list(map(int, input().split()))

while len(a) < n:
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)

k = [0] * 202
d, x = max(a), 0

for i in a:
    k[i] = 1

for i in range(1, d + 1):
    if not k[i]:
        x = 1
        print (i)

if not x:
    print ("Excellent!")

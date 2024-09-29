from math import sqrt


def kt(n):
    if n < 2:
        return 0
    x = int(sqrt(n)) + 1
    for i in range(2, x):
        if int(n % i) == 0:
            return 0
    return 1


n = int(input())
z = list(map(int, input().split()))
k = [0] * 1002
a = [0]

for i in z:
    if not k[i]:
        a.append(i)
        k[i] = 1

x = len(a) - 1
b = [0] * (x + 2)

for i in range(1, x + 1):
    b[i] = b[i - 1] + a[i]

d = 0
for i in range(1, x + 1):
    if kt(b[i]) and kt(b[x] - b[i]):
        d = 1
        print (i - 1)
        break

if not d:
    print ("NOT FOUND")

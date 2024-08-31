n = int(input())
a = list(map(int, input().split()))
k = [0] * 30002
for i in a:
    k[i] = 1

for i in range(1, n + 2):
    if not k[i]:
        print (i)
        break

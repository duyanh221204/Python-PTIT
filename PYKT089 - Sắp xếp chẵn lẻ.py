n = int(input())
a = list(map(int, input().split()))
while len(a) < n:
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)

odd, even = [], []

for i in a:
    if i & 1:
        odd.append(i)
    else:
        even.append(i)

even.sort()
odd.sort(reverse=True)

id1, id2 = 0, 0

for i in a:
    if i & 1:
        print (odd[id1], end=" ")
        id1 += 1
    else:
        print (even[id2], end=" ")
        id2 += 1

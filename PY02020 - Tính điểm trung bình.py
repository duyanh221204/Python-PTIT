n = int(input())
a = list(map(float, input().split()))

m1, m2 = min(a), max(a)
d, dem = 0.0, 0

for i in a:
    if i != m1 and i != m2:
        d += i
        dem += 1

print (f"{d / dem:.2f}")

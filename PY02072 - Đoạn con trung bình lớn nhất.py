n = int(input())
a = list(map(int, input().split()))
d = max(a)
ans, dem = 0, 0
for i in a:
    if i == d:
        dem += 1
    else:
        ans = max(dem, ans)
        dem = 0
print (max(ans, dem))

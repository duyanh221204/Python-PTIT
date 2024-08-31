a, k, n = map(int, input().split())
d = 0

for i in range(k - a % k, n - a + 1, k):
    d = 1
    print (i, end=" ")

if not d:
    print ("-1")

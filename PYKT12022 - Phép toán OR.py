n = int(input())
a = list(map(int, input().split()))
ss, s = set(), set()

for i in a:
    s1 = set()
    for j in s:
        ss.add(i | j)
        s1.add(i | j)
    ss.add(i)
    s1.add(i)
    s = s1

print (len(ss))

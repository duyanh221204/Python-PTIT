n = int(input())
a, s = [], [input() for _ in range(n)]
mp = dict()

d, h = 0, ""
for i in range(n):
    if s[i] != "":
        if not i or s[i - 1] == "":
            h = s[i]
            d = 0
            a.append(s[i])
            mp[s[i]] = 0
        else:
            mp[h] += 1

for i in a:
    print (f"{i}: {mp.get(i)}")

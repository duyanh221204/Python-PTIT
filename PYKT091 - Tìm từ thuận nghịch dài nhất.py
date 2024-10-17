def kt(s):
    return s == s[::-1]


a, d = [], 0
mp = dict()

with open("VANBAN.in") as file:
    s = file.readline()
    while s:
        s = s.split()
        for i in s:
            if kt(i):
                d = max(len(i), d)
                if mp.get(i) is None:
                    mp[i] = 0
                    a.append(i)
                mp[i] += 1
        s = file.readline()

for i in a:
    if len(i) == d:
        print (i, mp[i])

mp = dict()
a = []
n = int(input())

while n:
    s = input().split()
    if mp.get(s[4]) is None:
        mp[s[4]] = 0
        a.append(s[4])
    if s[3] == "IN":
        if s[1] == "Xe_con":
            if s[2] == "5":
                mp[s[4]] += 10000
            else:
                mp[s[4]] += 15000
        elif s[1] == "Xe_tai":
            mp[s[4]] += 20000
        else:
            if s[2] == "29":
                mp[s[4]] += 50000
            else:
                mp[s[4]] += 70000
    n -= 1

for i in a:
    print (f"{i}: {mp.get(i)}")

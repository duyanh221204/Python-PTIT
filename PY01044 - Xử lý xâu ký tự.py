s1 = input().split()
s2 = input().split()

ss1, ss2 = set(), set()

for i in s1:
    ss1.add(i.lower())

for i in s2:
    ss2.add(i.lower())

print (*sorted(ss1 | ss2))
print (*sorted(ss1 & ss2))

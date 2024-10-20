s1, s2 = set(), set()

with open("DATA1.in") as file:
    s = file.readline()
    while s:
        s = s.strip().lower().split()
        for i in s:
            s1.add(i)
        s = file.readline()

with open("DATA2.in") as file:
    s = file.readline()
    while s:
        s = s.strip().lower().split()
        for i in s:
            s2.add(i)
        s = file.readline()

print (*sorted(s1 - s2))
print (*sorted(s2 - s1))

s = input()
d1, d2 = 0, 0
for i in s:
    if i.islower():
        d1 += 1
    if i.isupper():
        d2 += 1

print (s.lower() if d1 >= d2 else s.upper())

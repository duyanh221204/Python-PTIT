s = input()
a = []
x = 0

while x + 1 < len(s):
    a.append(int(s[x:x+2]))
    x += 2

print (*list(sorted(set(a))))

def tt(s):
    d = 0
    for i in range(len(s) - 1, -1, -1):
        d += ((ord(s[i]) - 48) * (1 << (len(s) - i - 1)))
    return d


s = input()

while len(s) % 3:
    s = "0" + s

d = ""
for i in range(0, len(s), 3):
    d += str(tt(s[i:i+3]))

print (d)

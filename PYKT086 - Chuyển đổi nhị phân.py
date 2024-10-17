from math import log2

a = [str(i) for i in range(10)]
for i in range(10, 16):
    a.append(str(chr(i + 55)))


def tinh(x):
    d = 0
    for i in range(len(x)):
        d += ((ord(x[i]) - 48) * (1 << (len(x) - i - 1)))
    return d


def tt(x, b):
    c = int(log2(b))
    while int(len(x) % c) > 0:
        x = "0" + x
    s = ""
    for i in range(0, len(x), c):
        s += a[tinh(x[i:i+c])]
    return s


with open("DATA.in") as file:
    for T in range(int(file.readline().strip())):
        b = int(file.readline().strip())
        x = file.readline().strip()
        print (x if b == 2 else tt(x, b))

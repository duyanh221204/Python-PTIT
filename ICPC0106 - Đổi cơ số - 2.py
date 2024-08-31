from math import log2

a = [str(i) for i in range(10)]
for i in range(10, 16):
    a.append(str(chr(i + 55)))

def tinh(x):
    s = 0
    for i in range(len(x)):
        s += ((ord(x[i]) - 48) * (1 << i))
    return s

def tt(x, b):
    c = int(log2(b))
    x = x[::-1]
    while len(x) % c > 0:
        x += "0"
    s = ""
    for i in range(0, len(x), c):
        tmp = x[i:i+c]
        s += a[tinh(tmp)]
    return s[::-1]

for T in range(int(input())):
    b = int(input())
    x = input()
    print (x if b == 2 else tt(x, b))

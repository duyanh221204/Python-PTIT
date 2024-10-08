def tt(a):
    if a[0] == a[1] == a[2] == a[3]:
        return 0
    b = []
    for i in range(3):
        b.append(abs(a[i] - a[i + 1]))
    b.append(abs(a[3] - a[0]))
    return tt(b) + 1


while True:
    a = list(map(int, input().split()))
    if not a[0] and not a[1] and not a[2] and not a[3]:
        break
    print (tt(a))

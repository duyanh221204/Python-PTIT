a = []
mp = dict()

for i in range(60):
    for j in range(40):
        for k in range(30):
            x = (2 ** i) * (3 ** j) * (5 ** k)
            if mp.get(x) is None:
                mp[x] = 1
                a.append(x)

a.sort()

def tt(x):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = l + r >> 1
        if a[mid] == x:
            return mid + 1
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

for T in range(int(input())):
    n = int(input())
    id = tt(n)
    if id == -1:
        print ("Not in sequence")
    else:
        print (id)

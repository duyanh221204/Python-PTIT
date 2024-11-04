a, s = [], []
b = [0] * 20


def tt(x, n, k):
    for i in range(b[x - 1] + 1, n - k + x + 1, 1):
        b[x] = i
        if x == k:
            s1 = ""
            for j in range(1, k + 1, 1):
                s1 += (a[b[j] - 1] + " ")
            s.append(s1.strip())
        else:
            tt(x + 1, n, k)


n, k = map(int, input().split())
ss = sorted(set(input().split()))

for i in ss:
    a.append(i)

tt(1, len(a), k)

s.sort()

for i in s:
    print (i)

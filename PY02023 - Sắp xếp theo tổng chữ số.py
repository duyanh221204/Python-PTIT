def tt(n):
    s = 0
    while n:
        s += int(n % 10)
        n //= 10
    return s

for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (tt(x), x))
    print (*a)

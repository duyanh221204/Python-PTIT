from math import gcd

for T in range(int(input())):
    n = int(input())
    k = int(str(n)[::-1])
    print ("YES" if gcd(n, k) == 1 else "NO")

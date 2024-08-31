from math import sqrt

for T in range(int(input())):
    n = int(input())
    print ("1 ", end="")
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            m = 0
            while n % i == 0:
                m += 1
                n //= i
            print (f"* {i}^{m} ", end="")
    if n > 1:
        print (f"* {n}^1", end="")
    print ()

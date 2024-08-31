for T in range(int(input())):
    n = int(input())
    d = 1
    while n > 10:
        if n % 10 >= 5:
            n += 10
        d *= 10
        n //= 10
    print (d * n)

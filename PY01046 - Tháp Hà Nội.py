def tt(n, a, b, c):
    if n == 1:
        print (f"{a} -> {c}")
    else:
        tt(n - 1, a, c, b)
        tt(1, a, b, c)
        tt(n - 1, b, a, c)

tt(int(input()), "A", "B", "C")

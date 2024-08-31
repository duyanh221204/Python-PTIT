ss = set()

while True:
    try:
        a = list(map(int, input().strip().split()))
        for i in a:
            ss.add(int(i % 42))
    except EOFError:
        break

print (len(ss))

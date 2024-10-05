n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

print (*sorted(a & b))
print (*sorted(a - b))
print (*sorted(b - a))

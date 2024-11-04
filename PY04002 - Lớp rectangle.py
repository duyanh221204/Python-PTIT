class Rectangle:
    def __init__(self, w, h, c):
        self.w = w
        self.h = h
        self.c = c.title()

    def __str__(self):
        return f"{self.w + self.h << 1} {self.w * self.h} {self.c}"


a = list(map(str, input().split()))
if int(a[0]) <= 0 or int(a[1]) <= 0:
    print ("INVALID")
else:
    print (Rectangle(int(a[0]), int(a[1]), a[2]))

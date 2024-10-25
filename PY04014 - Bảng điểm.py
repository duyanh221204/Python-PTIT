from decimal import Decimal, ROUND_HALF_UP


class Student:
    def __init__(self, code, name, mark):
        self.code = f"HS{code:02d}"
        self.name = name
        self.mark = sum(mark) / 12
        if self.mark >= 9:
            self.status = "XUAT SAC"
        elif self.mark >= 8:
            self.status = "GIOI"
        elif self.mark >= 7:
            self.status = "KHA"
        elif self.mark >= 5:
            self.status = "TB"
        else:
            self.status = "YEU"

    def __str__(self):
        return f"{self.code} {self.name} {self.mark.quantize(Decimal('0.1'), ROUND_HALF_UP)} {self.status}"


n = int(input())
a = []

for i in range(n):
    s = input()
    b = list(map(Decimal, input().split()))
    b[0] = b[0] * 2
    b[1] = b[1] * 2
    a.append(Student(i + 1, s, b))

a.sort(key=lambda x: (-x.mark, x.code))

for i in a:
    print (i)

class DS:
    def __init__(self, ma, ten, m):
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        if 0 <= m <= 50:
            self.m = m * 100 * 1.02
        elif m <= 100:
            self.m = (5000 + (m - 50) * 150) * 1.03
        else:
            self.m = (12500 + (m - 100) * 200) * 1.05

    def __str__(self):
        return f"{self.ma} {self.ten} {round(self.m)}"


a = []
for i in range(int(input())):
    a.append(DS(i + 1, input(), abs(int(input()) - int(input()))))

a.sort(key=lambda x: (-x.m))

for i in a:
    print (i)

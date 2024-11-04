class Employee:
    def __init__(self, code, name, th, pr):
        self.code = f"TS0{code}"
        self.name = name
        if th > 10:
            th /= 10
        if pr > 10:
            pr /= 10
        self.mark = (th + pr) / 2
        if self.mark < 5:
            self.status = "TRUOT"
        elif self.mark < 8:
            self.status = "CAN NHAC"
        elif self.mark < 9.5:
            self.status = "DAT"
        else:
            self.status = "XUAT SAC"

    def __str__(self):
        return f"{self.code} {self.name} {self.mark:.2f} {self.status}"


a = []
for i in range(int(input())):
    a.append(Employee(i + 1, input(), float(input()), float(input())))

a.sort(key=lambda x: -x.mark)

for i in a:
    print (i)

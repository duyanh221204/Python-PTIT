class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop
        self.cc = 10

    def tt(self, s):
        for i in s:
            if i == "m":
                self.cc -= 1
            if i == "v":
                self.cc -= 2
        if self.cc < 0:
            self.cc = 0

    def __str__(self):
        s = self.msv + " " + self.ten + " " + self.lop + " " + str(self.cc)
        if not self.cc:
            s += " KDDK"
        return s


a = []
mp = dict()
n = int(input())
for i in range(n):
    msv = input()
    ten = input()
    lop = input()
    dt = SinhVien(msv, ten, lop)
    a.append(dt)
    mp[dt.msv] = dt

for i in range(n):
    s = input().split()
    mp[s[0]].tt(s[1])

for i in a:
    print (i)

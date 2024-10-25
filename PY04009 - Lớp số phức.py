class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def add(self, a):
        return SoPhuc(self.thuc + a.thuc, self.ao + a.ao)

    def mul(self, a):
        return SoPhuc(self.thuc * a.thuc - self.ao * a.ao, self.thuc * a.ao + self.ao * a.thuc)

    def __str__(self):
        s = str(self.thuc)
        if self.ao >= 0:
            s += (" + " + str(self.ao) + "i")
        else:
            s += (" - " + str(abs(self.ao)) + "i")
        return s


for T in range(int(input())):
    a = list(map(int, input().split()))
    while len(a) < 4:
        b = list(map(int, input().split()))
        for i in b:
            a.append(i)
    x, y = SoPhuc(a[0], a[1]), SoPhuc(a[2], a[3])
    print ((x.add(y)).mul(x), end=", ")
    print ((x.add(y)).mul(x.add(y)))

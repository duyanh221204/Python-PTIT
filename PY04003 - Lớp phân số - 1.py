from math import gcd


class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m

    def rutGon(self):
        mc = gcd(self.t, self.m)
        self.t //= mc
        self.m //= mc
        return f"{self.t}/{self.m}"


t, m = map(int, input().split())
p = PhanSo(t, m)
print (p.rutGon())

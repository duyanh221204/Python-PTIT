from math import gcd


class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m

    def rutGon(self):
        mc = gcd(self.t, self.m)
        self.t //= mc
        self.m //= mc
        return self

    def add(self, p):
        mc = self.m * p.m // gcd(self.m, p.m)
        tt = self.t * (mc // self.m) + p.t * (mc // p.m)
        mt = mc
        return PhanSo(tt, mt).rutGon()

    def __str__(self):
        return f"{self.t}/{self.m}"


tp, mp, tq, mq = map(int, input().split())
p, q = PhanSo(tp, mp), PhanSo(tq, mq)
print (p.add(q))

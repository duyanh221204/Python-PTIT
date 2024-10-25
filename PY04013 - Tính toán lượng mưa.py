class DS:
    def __init__(self, ma, tram, thoiGian, luongMua):
        self.ma = f"T{ma:02d}"
        self.tram = tram
        self.thoiGian = thoiGian
        self.luongMua = luongMua

    def __str__(self):
        return f"{self.ma} {self.tram} {self.luongMua*60/self.thoiGian:.2f}"
    

a = []
for i in range(int(input())):
    s = input()
    g, p = map(int, input().split(":"))
    st = g * 60 + p
    g, p = map(int, input().split(":"))
    en = g * 60 + p
    m = int(input())
    d = 0
    for j in a:
        if j.tram == s:
            d = 1
            j.luongMua += m
            j.thoiGian += (en - st)
            break
    if not d:
        a.append(DS(i + 1, s, en - st, m))

for i in a:
    print (i)

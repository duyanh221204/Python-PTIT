from datetime import datetime


class Movie:
    def __init__(self, code, kind, date, name, episode):
        self.code = f"P{code:03d}"
        self.kind = kind
        self.date = date
        self.name = name
        self.episode = episode
        self.time = datetime.strptime(date, "%d/%m/%Y")

    def __str__(self):
        return f"{self.code} {self.kind} {self.date} {self.name} {self.episode}"


n, m = map(int, input().split())
mp = dict()

for i in range(n):
    mp[f"TL{(i+1):03d}"] = input()

a = []
for i in range(m):
    a.append(Movie(i + 1, mp[input()], input(), input(), int(input())))

a.sort(key=lambda x: (x.time, x.name, -x.episode))

for i in a:
    print (i)

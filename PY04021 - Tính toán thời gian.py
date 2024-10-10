from datetime import datetime


class Player:
    def __init__(self, code, name, time_in, time_out):
        self.code = code
        self.name = name
        self.time_in = time_in
        self.time_out = time_out
        self.hour, self.minute = self.calc()

    def calc(self):
        IN, OUT = datetime.strptime(self.time_in, "%H:%M"), datetime.strptime(self.time_out, "%H:%M")
        time = OUT - IN
        return time.seconds // 3600, int(time.seconds % 3600) // 60

    def __str__(self):
        return f"{self.code} {self.name} {self.hour} gio {self.minute} phut"


n = int(input())
a = []
while n:
    a.append(Player(input(), input(), input(), input()))
    n -= 1

a.sort(key=lambda x: (-x.hour, -x.minute))

for i in a:
    print (i)

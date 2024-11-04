from datetime import datetime


class Room:
    def __init__(self, code, name, roomNum, start, end, incurredCost):
        self.code = f"KH{code:02d}"
        self.name = name
        self.roomNum = roomNum
        st = datetime.strptime(start, "%d/%m/%Y")
        en = datetime.strptime(end, "%d/%m/%Y")
        self.day = (en - st).days + 1
        tmp = str(roomNum)[0]
        if ord(tmp) == 49:
            self.totalCost = 25 * self.day
        elif ord(tmp) == 50:
            self.totalCost = 34 * self.day
        elif ord(tmp) == 51:
            self.totalCost = 50 * self.day
        else:
            self.totalCost = 80 * self.day
        self.totalCost += incurredCost

    def __str__(self):
        return f"{self.code} {self.name} {self.roomNum} {self.day} {self.totalCost}"


a = []
for i in range(int(input())):
    a.append(Room(i + 1, input().strip(), int(input().strip()), input().strip(), input().strip(), int(input().strip())))

a.sort(key=lambda x: -x.totalCost)

for i in a:
    print (i)

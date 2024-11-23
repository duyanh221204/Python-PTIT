class Student:
    def __init__(self, id, name, team):
        self.id = f"C{id:03d}"
        self.name = name
        self.team = team

    def __str__(self):
        return f"{self.id} {self.name} {self.team}"


n = int(input())
mp = dict()

for i in range(n):
    mp[f"Team{i+1:02d}"] = input() + " " + input()

m = int(input())
a = []

for i in range(m):
    a.append(Student(i + 1, input(), mp[input()]))

a.sort(key=lambda x: x.name)

for i in a:
    print (i)

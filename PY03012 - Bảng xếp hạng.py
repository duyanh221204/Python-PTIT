class Student:
    def __init__(self, name, accept, submit):
        self.name = name
        self.accept = accept
        self.submit = submit

    def __str__(self):
        return f"{self.name} {self.accept} {self.submit}"


n = int(input())
a = []

for i in range(n):
    name = input()
    accept, submit = map(int, input().split())
    a.append(Student(name, accept, submit))

a.sort(key=lambda x: (-x.accept, x.submit, x.name))

for i in a:
    print (i)

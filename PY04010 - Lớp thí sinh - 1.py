class Student:
    def __init__(self, name, dob, d1, d2, d3):
        self.name = name
        self.dob = dob
        self.d = d1 + d2 + d3

    def __str__(self):
        return f"{self.name} {self.dob} {self.d:.1f}"


print (Student(input(), input(), float(input()), float(input()), float(input())))

from functools import cmp_to_key


class Contact:
    def __init__(self, name, phone, day):
        self.name = name
        self.phone = phone
        self.day = day


def cmp(a: Contact, b: Contact):
    name1, name2 = a.name.split(), b.name.split()
    if name1[-1] < name2[-1]:
        return -1
    if name1[-1] > name2[-1]:
        return 1
    if name1[-2] < name2[-2]:
        return -1
    if name1[-2] > name2[-2]:
        return 1
    return 0


a = []
name, day = "", ""
with open("SOTAY.txt") as file:
    line = file.readline().strip()
    while line:
        if line.startswith("Ngay"):
            day = line[5:]
        elif line[0].isalpha():
            name = line
        else:
            a.append(Contact(name, line, day))
        line = file.readline().strip()

a.sort(key=cmp_to_key(cmp))

with open("DIENTHOAI.txt", "w") as file:
    for i in a:
        file.write(f"{i.name}: {i.phone} {i.day}\n")

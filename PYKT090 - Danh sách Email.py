with open("CONTACT.in", "r") as file:
    a = [i.strip().lower() for i in file]

a = sorted(set(a))

for i in a:
    print (i)

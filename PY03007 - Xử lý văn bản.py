a = []

while True:
    try:
        s = input().lower().split()
        for i in s:
            a.append(i)
    except Exception:
        break

s = ""

for i in a:
    if i[-1] in ".?!":
        m = i.split(".")
        m = m[0].split("?")
        m = m[0].split("!")
        s += m[0]
        print (s[0].upper() + s[1:])
        s = ""
    else:
        s += (i + " ")
